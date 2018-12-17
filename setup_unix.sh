#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd)"
BAZEL_DOCKER_IMAGE_NAME="gcr.io/cloud-builders/bazel"

# Returns the Docker binary from $PATH or fails with a descriptive error message.
function test_docker_availability {
    local DOCKER_BINARY_PATH
    DOCKER_BINARY_PATH=`which docker`
    if [[ $? -ne 0 ]]; then
        echo "[ERROR]: Unable to find docker in your system. Did you installed it ?"
        exit 1
    fi
}

# Checks if Bazel is currently installed on the host. If not, it fallbacks setting up a containerized version of Bazel
# using Docker and a Linux alias.
function test_bazel_availability {
    unalias bazel > /dev/null 2>&1
    local BAZEL_OUTPUT_ROOT
    local BAZEL_EXISTS
    BAZEL_OUTPUT_ROOT="${HOME}/.cache/bazel"
    BAZEL_EXISTS=`which bazel`
    if [[ $? -ne 0 ]]; then
        IMAGE_ID=`$(which docker) images ${BAZEL_DOCKER_IMAGE_NAME} -q`
        if [[ -z "${IMAGE_ID}" ]]; then
            $(which docker) pull "${BAZEL_DOCKER_IMAGE_NAME}"
            IMAGE_ID=`$(which docker) images ${BAZEL_DOCKER_IMAGE_NAME} -q`
        fi
        mkdir -p "${BAZEL_OUTPUT_ROOT}"
        alias bazel="$(which docker) run --rm -it \
            -w /workspace \
            -v ${SCRIPT_DIR}:/workspace \
            ${IMAGE_ID}"
    fi
}

test_docker_availability
test_bazel_availability

# Unset helper functions + variables to prevent them from showing up on SHELL auto-complete.
unset test_docker_availability
unset test_bazel_availability
unset autogenerate_bazelrc
