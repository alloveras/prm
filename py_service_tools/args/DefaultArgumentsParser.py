import argparse
import socket


class DefaultArgumentsParser(object):
    _DEFAULT_STAGES = ["local", "beta", "prod"]
    # The most obvious thing would be to default GRPC_ADDR to either "localhost" or
    # "127.0.0.1". However, since most of the times services run within Docker containers
    # it's safer to rely on DNS hostname resolution to retrieve the loca IP address.
    _DEFAULT_GRPC_ADDR = socket.gethostbyname(socket.gethostname())
    _DEFAULT_GRPC_PORT = 50051

    def __init__(self, description, argv):
        self._args = self.__parse_arguments(description, argv)

    def get_stage(self):
        return self._args.stage

    def get_grpc_address(self):
        return self._args.grpc_address

    def get_grpc_port(self):
        return self._args.grpc_port

    def should_enable_grpc_ssl(self):
        return "local" != self.get_stage()

    def get_ssl_certs_root(self):
        return self._args.ssl_certs_root

    def _define_custom_arguments(self, parser):
        # Nothing to do here. This is only to allow child classes add
        # extra arguments to parse depending on their particular use-cases.
        pass

    def __define_default_arguments(self, parser):
        parser.add_argument("--stage", type=str, required=True, choices=self._DEFAULT_STAGES)
        parser.add_argument("--grpc-address", type=str, default=self._DEFAULT_GRPC_ADDR, required=False)
        parser.add_argument("--grpc-port", type=self._argparse_check_positive, default=self._DEFAULT_GRPC_PORT,
                            required=False)
        parser.add_argument("--ssl-certs-root", type=str, required=False)

    def __parse_arguments(self, description, argv):
        parser = argparse.ArgumentParser(description=description)
        self.__define_default_arguments(parser)
        self._define_custom_arguments(parser)
        return parser.parse_args(argv[1:])

    @staticmethod
    def _argparse_check_positive(value):
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError("% is not a positive number bigger than 0" % value)
        return int_value
