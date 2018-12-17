load("@build_stack_rules_proto//python:python_grpc_library.bzl", "python_grpc_library")

proto_library(
    name = "service_proto",
    srcs = [ "service.proto" ],
    deps = [
        "//uuid_service_protos/operations:create_uuid_proto",
    ],
    visibility = [ "//visibility:private" ]
)

python_grpc_library(
    name = "uuid_service_py_proto",
    deps = [ ":service_proto" ],
    visibility = [ "//visibility:public" ]
)