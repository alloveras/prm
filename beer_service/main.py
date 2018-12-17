#!/usr/bin/env python


from clients import ClientsFactory
from py_service_tools import LoggingHelper, ServiceRunner
from repository import RepositoryFactory
from service import BeerService, BeerServiceArgumentsParser


def main(args):
    logger = LoggingHelper.init_root_logger()
    logger = LoggingHelper.add_stdout_logger(logger)
    service = BeerService(logger, RepositoryFactory(args), ClientsFactory(args))
    service_runner = ServiceRunner(args, service.get_grpc_binding_function())
    service_runner.run()


if __name__ == "__main__":
    main(BeerServiceArgumentsParser())
