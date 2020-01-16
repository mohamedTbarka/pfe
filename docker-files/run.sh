#!/bin/bash
PROJECT_PATH=`pwd`
DEPLOY_ENV_FILE="$PROJECT_PATH/docker-files/deploy.env"
CONFIG_ENV_FILE="$PROJECT_PATH/docker-files/secrets/config.env"
TICKER=$1
TAG=$2
UID=$(awk -F "=" '/UID/ {print $2}' $DEPLOY_ENV_FILE)
GID=$(awk -F "=" '/GID/ {print $2}' $DEPLOY_ENV_FILE)
CONTAINER_PORT=$(awk -F "=" '/CONTAINER_PORT/ {print $2}' $DEPLOY_ENV_FILE)
RUNSERVER_PORT=$(awk -F "=" '/RUNSERVER_PORT/ {print $2}' $DEPLOY_ENV_FILE)
STATIC_ROOT="$PROJECT_PATH/static_root"
MEDIA_ROOT="$PROJECT_PATH/app/media"
if [ -f $CONFIG_ENV_FILE ]; then
docker run -d --user $UID:$GID -p $CONTAINER_PORT:8000 -p $RUNSERVER_PORT:8001 --env-file $CONFIG_ENV_FILE -v $STATIC_ROOT:/static_root -v $MEDIA_ROOT:/src/media --name $TICKER $TAG
else
docker run -d --user $UID:$GID -p $CONTAINER_PORT:8000 -p $RUNSERVER_PORT:8001 -v $STATIC_ROOT:/static_root -v $MEDIA_ROOT:/src/media --name $TICKER $TAG
fi
