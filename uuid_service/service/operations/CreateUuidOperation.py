import uuid

from uuid_service_protos.operations.create_uuid_pb2 import CreateUuidResponse


class CreateUuidOperation:

    def __init__(self):
        pass

    @staticmethod
    def execute(request, context):
        res = CreateUuidResponse()
        res.uuid = str(uuid.uuid4())
        return res
