FROM python:3.9-alpine

RUN apk add --no-cache curl tar g++ make libffi-dev openssl-dev python3-dev \
    && pip install 'poetry==1.1.4' \
    && mkdir -p /opt/ \
    && curl -L https://github.com/nicos68/telegram-scheduling/archive/master.tar.gz | tar zxvf - -C /opt/ \
    && mv /opt/telegram-scheduling-master /opt/telegram-scheduling \
    && cd /opt/telegram-scheduling \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && rm -rf /opt/meteo-bot/tests
