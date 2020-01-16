#!/bin/bash
APP_NAME=$1
make stop;make run
docker exec $APP_NAME env/bin/python manage.py test
