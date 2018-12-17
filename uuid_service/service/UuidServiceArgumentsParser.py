import sys

from py_service_tools import ServiceArgumentsParser


class UuidServiceArgumentsParser(ServiceArgumentsParser):

    def __init__(self):
        ServiceArgumentsParser.__init__(self, "UUID Service", sys.argv)
