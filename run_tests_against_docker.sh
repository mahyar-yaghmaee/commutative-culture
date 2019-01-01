#!/usr/bin/env bash

set -o nounset
set -o errexit

./build.sh
./run_build.sh
/usr/local/bin/docker exec -it commutative-culture python3 -m unittest
./clean-docker.sh