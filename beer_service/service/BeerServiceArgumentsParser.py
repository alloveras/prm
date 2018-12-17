import sys

from py_service_tools import ServiceArgumentsParser


class BeerServiceArgumentsParser(ServiceArgumentsParser):

    def __init__(self):
        super(BeerServiceArgumentsParser, self).__init__("Beer Service", sys.argv)

    def get_uuid_service_config(self):
        return self._args.uuid_service_address, self._args.uuid_service_port, self._args.uuid_service_ssl_cert_path

    def _define_custom_arguments(self, parser):
        super(BeerServiceArgumentsParser, self)._define_custom_arguments(parser)
        parser.add_argument("--uuid-service-address", type=str, required=True)
        parser.add_argument("--uuid-service-port", type=self._argparse_check_positive, default=50051, required=False)
        parser.add_argument("--uuid-service-ssl-cert-path", type=str, required=False)
