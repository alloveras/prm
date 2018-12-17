load("@build_stack_rules_proto//python:python_grpc_library.bzl", "python_grpc_library")

proto_library(
    name = "service_proto",
    srcs = [ "service.proto" ],
    deps = [
        "//beer_service_protos/operations:create_beer_proto",
        "//beer_service_protos/operations:list_all_beers_proto",
        "//beer_service_protos/operations:get_beer_by_id_proto",
        "//beer_service_protos/domain:beer_proto"
    ],
    visibility = [ "//protos:__pkg__" ]
)

python_grpc_library(
    name = "beer_service_py_proto",
    deps = [ ":service_proto" ],
    visibility = [ "//visibility:public" ]
)

