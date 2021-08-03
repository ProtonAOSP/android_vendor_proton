#!/usr/bin/env bash

set -eufo pipefail

cat "$1" | \
    head -n-1 | \
    sed 1d | \
    base64 -d | \
    xxd -p | \
    tr -d '\n'
