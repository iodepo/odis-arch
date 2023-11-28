#!/bin/bash

# gleaner-cli 
# A wrapper script for invoking gleaner-cli with docker
# Put this script in $PATH as `rgleaner-cli`
# TODO 
# add help with things like config for 
# go run ../../cmd/gleaner/main.go -cfg eco_local -source '{"Name":"opentopo", "URL":"https://portal.opentopography.org/sitemap.xml", "Headless":false, "PID":"http://doi.org/10.17616/R3J616"}'



PROGNAME="$(basename $0)"
VERSION="v0.0.1"

# Pull down some of the needed docks if called with -init
if [[ $1 == "-init" ]];
then 
    curl -O https://schema.org/version/latest/schemaorg-current-https.jsonld
    curl -O https://raw.githubusercontent.com/earthcubearchitecture-project418/gleaner/master/configs/demo.yaml
    curl -O https://raw.githubusercontent.com/earthcubearchitecture-project418/gleaner/master/deployment/setenvIS.sh
    curl -O https://raw.githubusercontent.com/earthcubearchitecture-project418/gleaner/master/deployment/gleaner-IS.yml
    docker pull fils/gleaner:latest
    echo "\n See notes at: https://github.com/earthcubearchitecture-project418/gleaner/blob/dev/docs/cliDocker/README.md \n"
    exit 0
fi

# Helper functions for guards
error(){
  error_code=$1
  echo "ERROR: $2" >&2
  echo "($PROGNAME wrapper version: $VERSION, error code: $error_code )" &>2
  exit $1
}
check_cmd_in_path(){
  cmd=$1
  which $cmd > /dev/null 2>&1 || error 1 "$cmd not found!"
}

# Guards (checks for dependencies)
check_cmd_in_path docker
check_cmd_in_path curl

# Set up mounted volumes, environment, and run our containerized command
# podman needs --privileged to mount /dev/shm
#exec podman run \
  #--privileged \
  #--interactive --tty --rm \
  #--volume "$PWD":/wd \
  #--workdir /wd \
  #"localhost/nsfearthcube/gleaner:latest" "$@"

exec docker run \
  --interactive --tty --rm \
  --volume "$PWD":/wd \
  --workdir /wd \
  "fils/gleaner:latest" "$@"

