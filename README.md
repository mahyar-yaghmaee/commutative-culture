# commutative-culture

This is based on python 3 (since Heroku runs on python 3)

## Running tests locally
```
./run_tests_locally.sh
```

## Running tests against a docker container (make sure there's no `commutative-culture` container already running.
```
./run_tests_against_docker.sh
```

## Run the app locally on docker container
Need to install/run docker on mac (need to have an account on docker hub) : https://docs.docker.com/docker-for-mac/install/

- build the image:
```
./build.sh
```
- run the container:
```
run_build.sh
```

Run `clean-docker.sh` to stop/remove the container
