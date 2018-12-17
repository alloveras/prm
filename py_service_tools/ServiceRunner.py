import logging
import os
import signal

import grpc
from concurrent import futures


class ServiceRunner:
    _ONE_DAY_IN_SECONDS = 24 * 3600
    _GRACE_PERIOD_SECONDS = 10
    _SSL_PRIVATE_KEY_FILE_NAME = "private.key"
    _SSL_CERTIFICATE_CHAIN_FILE_NAME = "chain.crt"

    def __init__(self, args_parser, binding_func):
        self._wait = True
        self._service_name = args_parser.get_service_name()
        self._address = "%s:%s" % (args_parser.get_grpc_address(), args_parser.get_grpc_port())
        self._server = self._create_grpc_server(self._address, args_parser, binding_func)
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)

    def run(self):
        logging.info("Starging %s...", self._service_name)
        self._server.start()
        logging.info("%s started and listening on %s", self._service_name, self._address)
        while self._wait:
            signal.pause()
        self._wait = True
        logging.info("%s stopped", self._service_name)

    def _signal_handler(self, signum, frame):
        if signum == signal.SIGINT:
            # If the process receives a keyboard interrupt (Ctrl + C)
            # then we shutdown the service instantaenously without
            # grace period.
            logging.info("SIGINT (Ctrl+C) received. Stopping %s without grace period...", self._service_name)
            self._server.stop(0).wait()
            self._wait = False
        elif signum == signal.SIGTERM:
            # If the process receives a termination interrupt then we shutdown the service with a grace period
            # which, by default, is set to 10 seconds (Docker's stop default waiting time).
            logging.warning("SIGTERM received. Stopping %s but waiting %d seconds of grace period...", self._service_name,
                            self._GRACE_PERIOD_SECONDS)
            self._server.stop(self._GRACE_PERIOD_SECONDS).wait()
            self._wait = False
        else:
            # For any other signal, don't do anything and
            # return as quick as posible.
            pass

    @staticmethod
    def _create_grpc_server(address, args_parser, add_to_server_func):
        if args_parser.should_enable_grpc_ssl():
            return ServiceRunner._create_secure_grpc_server(address, args_parser, add_to_server_func)
        else:
            return ServiceRunner._create_insecure_grpc_server(address, args_parser, add_to_server_func)

    @staticmethod
    def _create_secure_grpc_server(address, args_parser, add_to_server_func):
        certs_root = os.path.normpath(args_parser.get_ssl_certs_root())
        certs_root = os.path.join(certs_root, "%s.%s" % (args_parser.get_service_name().lower(), args_parser.get_stage().lower()))

        private_key_file = os.path.join(certs_root, ServiceRunner._SSL_PRIVATE_KEY_FILE_NAME)
        certificate_chain_file = os.path.join(certs_root, ServiceRunner._SSL_CERTIFICATE_CHAIN_FILE_NAME)

        with open(private_key_file, 'rb') as private_key_handle, open(certificate_chain_file, 'rb') as certificate_chain_handle:
            credentials_tuple = (private_key_handle.read(), certificate_chain_handle.read())

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=args_parser.get_grpc_max_workers()))
        add_to_server_func(server)
        server_credentials = grpc.ssl_server_credentials(credentials_tuple)
        server.add_secure_port(address, server_credentials)
        return server

    @staticmethod
    def _create_insecure_grpc_server(address, args_parser, add_to_server_func):
        max_workers = args_parser.get_grpc_max_workers()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="grpc-server-thread"))
        add_to_server_func(server)
        server.add_insecure_port(address)
        return server
