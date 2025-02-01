#!/bin/bash

#docker rm -f registry-service
#docker build . -t mlp-registry -f registry-service/Dockerfile
#
#docker rm -f reactor
#docker build . -t mlp-reactor -f reactor/Dockerfile

docker-compose -f ./docker-compose.yaml --project-directory . up -d --remove-orphans