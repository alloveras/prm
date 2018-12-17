workspace(name = "production_ready_microservices")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

##################################################################################################################################
# Fetch Google Protobuff compiler
##################################################################################################################################
http_archive(
    name = "com_google_protobuf",
    sha256 = "d7a221b3d4fb4f05b7473795ccea9e05dab3b8721f6286a95fffbffc2d926f8b",
    strip_prefix = "protobuf-3.6.1",
    urls = ["https://github.com/google/protobuf/archive/v3.6.1.zip"],
)

##################################################################################################################################
# Fetch GoogleAPIs Protobuff definitions
##################################################################################################################################
GOOGLE_APIS_BUILD_FILE = """
package(default_visibility = ["//visibility:public"])

proto_library(
    name = "grpc_status_proto",
    srcs = ["google/rpc/status.proto"],
    deps = ["@com_google_protobuf//:any_proto"],
)

proto_library(
    name = "grpc_error_details_proto",
    srcs = ["google/rpc/error_details.proto"],
    deps = ["@com_google_protobuff//:duration_proto"]
)

proto_library(
    name = "grpc_code_proto",
    srcs = ["google/rpc/code.proto"]
)
"""

http_archive(
    name = "com_google_googleapis",
    build_file_content = GOOGLE_APIS_BUILD_FILE,
    sha256 = "3ff2365822fb573cb1779ada5c2ac7899269cacd0836aef95ffe9d95779031f2",
    strip_prefix = "googleapis-common-protos-1_3_1",
    url = "https://github.com/googleapis/googleapis/archive/common-protos-1_3_1.zip",
)

##################################################################################################################################
# Fetch StackB Bazel rules from https://github.com/stackb/rules_proto/
##################################################################################################################################
http_archive(
    name = "build_stack_rules_proto",
    urls = ["https://github.com/stackb/rules_proto/archive/4c2226458203a9653ae722245cc27e8b07c383f7.tar.gz"],
    sha256 = "0be90d609fcefae9cc5e404540b9b23176fb609c9d62f4f9f68528f66a6839bf",
    strip_prefix = "rules_proto-4c2226458203a9653ae722245cc27e8b07c383f7",
)

load("@build_stack_rules_proto//python:deps.bzl", "python_grpc_library")

python_grpc_library()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

pip_import(
	name = "protobuf_py_deps",
	requirements = "@build_stack_rules_proto//python:requirements.txt"
)

load("@protobuf_py_deps//:requirements.bzl", protobuf_pip_install = "pip_install")

protobuf_pip_install()

pip_import(
   name = "grpc_py_deps",
   requirements = "@build_stack_rules_proto//python:requirements.txt",
)

load("@grpc_py_deps//:requirements.bzl", grpc_pip_install = "pip_install")

grpc_pip_install()
