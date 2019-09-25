FROM python:3.7-alpine

LABEL container_name = "auth"
LABEL email="grutecfiap@hotmail.com"
LABEL created_at = "Sep 04 2019"

COPY . /app
WORKDIR /app

RUN apk add mariadb-dev
RUN apk add postgresql-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers python-dev build-base
RUN pip install --upgrade pip -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers=3", "--threads=3", "--reload", "server:app"]