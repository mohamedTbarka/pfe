#!/bin/bash
PROJECT_PATH=`pwd`
DEPLOY_ENV_FILE="$PROJECT_PATH/docker-files/deploy.env"
CONFIG_ENV_FILE="$PROJECT_PATH/.env"
TICKER=$1
UID=$(awk -F "=" '/UID/ {print $2}' $DEPLOY_ENV_FILE)
GID=$(awk -F "=" '/GID/ {print $2}' $DEPLOY_ENV_FILE)
CONTAINER_PORT=$(awk -F "=" '/CONTAINER_PORT/ {print $2}' $DEPLOY_ENV_FILE)
STATIC_ROOT="$PROJECT_PATH/static_root"
MEDIA_ROOT="$PROJECT_PATH/app/media"
docker exec -ti $TICKER bash -c ''
docker exec -ti $TICKER bash -c 'env/bin/python manage.py runserver 0.0.0.0:8001'
