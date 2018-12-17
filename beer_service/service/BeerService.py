#!/usr/bin/env python

from beer_service_protos.service_pb2_grpc import BeerServicer, add_BeerServicer_to_server


class BeerService(BeerServicer):

    def __init__(self, logger, repository_factory, clients_factory):
        self._logger = logger
        self._beer_repository = repository_factory.create_beer_repository()
        self._uuid_service_client = clients_factory.create_uuid_service_client()

    def ListAllBeers(self, request, context):
        pass

    def CreateBeer(self, request, context):
        pass

    def GetBeerById(self, request, context):
        pass

    def get_grpc_binding_function(self):
        return lambda server: add_BeerServicer_to_server(self, server)
