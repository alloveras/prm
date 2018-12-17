import grpc


class GrpcClientHelper:

    def __init__(self):
        # No-Op
        pass

    @staticmethod
    def create_channel(address, port, ssl_cert_path):
        if ssl_cert_path is None:
            return grpc.insecure_channel("%s:%d" % (address, port))
        else:
            ssl_cert_content = GrpcClientHelper._load_ssl_certificate(ssl_cert_path)
            return grpc.ssl_channel_credentials(root_certificates=ssl_cert_content)

    @staticmethod
    def _load_ssl_certificate(ssl_cert_path):
        with open(ssl_cert_path) as ssl_certs_file:
            return ssl_certs_file.read()
