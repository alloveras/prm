#!/usr/bin/env python

from py_service_tools import ServiceRunner, LoggingHelper
from service import UuidService, UuidServiceArgumentsParser


def main(args):
    logger = LoggingHelper.init_root_logger()
    logger = LoggingHelper.add_stdout_logger(logger)
    service = UuidService(logger)
    service_runner = ServiceRunner(args, service.get_grpc_binding_function())
    service_runner.run()


if __name__ == "__main__":
    main(UuidServiceArgumentsParser())
