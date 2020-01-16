#!/bin/bash
APP_NAME=$1
DOCKER_CONTAINER_NAME=$(docker ps -a -q --filter "name=$APP_NAME")
if [ ! -z $DOCKER_CONTAINER_NAME ]; then
    docker stop $DOCKER_CONTAINER_NAME 
    docker rm $DOCKER_CONTAINER_NAME 
fi
