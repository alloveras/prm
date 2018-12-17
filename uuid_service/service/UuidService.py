from uuid_service_protos.service_pb2_grpc import UuidServicer, add_UuidServicer_to_server

from operations.CreateUuidOperation import CreateUuidOperation


class UuidService(UuidServicer):

    def __init__(self, logger):
        self._logger = logger

    @staticmethod
    def CreateUuid(request, context):
        return CreateUuidOperation().execute(request, context)

    def get_grpc_binding_function(self):
        return lambda server: add_UuidServicer_to_server(self, server)
