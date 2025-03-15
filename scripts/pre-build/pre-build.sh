#!/usr/bin/env bash

set -eo pipefail

echo "run pre-build.sh"

DIRNAME="$(dirname -- "${BASH_SOURCE[0]}")"

# "$DIRNAME"/install-theme.sh

git rev-parse --short HEAD | xargs -I % sed -i "s/githash: ''/githash: '%'/g" mkdocs.yml

node --loader ts-node/esm

echo "finish pre-build.sh"