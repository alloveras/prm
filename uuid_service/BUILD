py_library(
    name = "uuid_service_py_lib",
    srcs = glob(["service/**/*.py"]),
    deps = [
        "//uuid_service_protos:uuid_service_py_proto",
        "//py_service_tools"
    ],
    visibility = ["//visibility:public"]
)

py_binary(
    name = "uuid_service",
    srcs = [ "main.py" ],
    deps = [
        ":uuid_service_py_lib"
    ],
    main = "main.py",
    visibility = [ "//visibility:private" ]
)