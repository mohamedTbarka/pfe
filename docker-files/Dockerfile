FROM python:3.7.3-alpine3.9
RUN apk --update add --no-cache unrar make g++ libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc curl linux-headers \
mariadb-dev python3-dev postgresql-dev git bash imagemagick imagemagick-dev \
jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev gettext
RUN pip3 install --upgrade pip setuptools wheel
WORKDIR /src
RUN pip3 install virtualenv
RUN virtualenv -p python3 /src/env 
ADD requirements.pip /src
RUN /src/env/bin/pip install -r /src/requirements.pip && /src/env/bin/pip install gunicorn
ADD app /src
ADD docker-files/entrypoint.sh /src
RUN chmod u+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
