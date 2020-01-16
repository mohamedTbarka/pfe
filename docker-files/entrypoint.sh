#!/bin/sh
/src/env/bin/python manage.py collectstatic --noinput
/src/env/bin/python manage.py migrate
/src/env/bin/gunicorn --bind 0.0.0.0:8000 -w $WORKER_COUNT -t $THREAD_COUNT app.wsgi
