py_library(
    name = "beer_service_py_lib",
    srcs = glob([
        "clients/**/*.py",
        "domain/**/*.py",
        "repository/**/*.py",
        "service/**/*.py"
    ]),
    deps = [
        "//beer_service_protos:beer_service_py_proto",
        "//uuid_service_protos:uuid_service_py_proto",
        "//py_service_tools",
    ],
    visibility = [ "//visibility:private" ]
)

py_binary(
    name = "beer_service",
    srcs = [ "main.py" ],
    deps = [
        ":beer_service_py_lib",
    ],
    main = "main.py",
    visibility = [ "//visibility:private" ]
)

