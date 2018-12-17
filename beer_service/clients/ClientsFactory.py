#!/usr/bin/env python

from uuid_service_protos.service_pb2_grpc import UuidStub

from py_service_tools import GrpcClientHelper


class ClientsFactory:

    def __init__(self, args):
        self._args = args
        self._uuid_service_client = None

    def create_uuid_service_client(self):
        if self._uuid_service_client is None:
            address, port, ssl_cert_path = self._args.get_uuid_service_config()
            channel = GrpcClientHelper.create_channel(address, port, ssl_cert_path)
            self._uuid_service_client = UuidStub(channel)
        return self._uuid_service_client
