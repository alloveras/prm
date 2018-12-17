from py_service_tools.args import DefaultArgumentsParser


class ServiceArgumentsParser(DefaultArgumentsParser):

    def __init__(self, service_name, argv):
        super(ServiceArgumentsParser, self).__init__(service_name, argv)
        self._service_name = service_name

    def get_service_name(self):
        return self._service_name

    def get_grpc_max_workers(self):
        return self._args.grpc_max_workers

    def _define_custom_arguments(self, parser):
        parser.add_argument("--grpc-max-workers", type=self._argparse_check_positive, default=10, required=False)
