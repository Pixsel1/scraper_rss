FROM python:3.7.3-alpine

RUN apk update && apk --no-cache add \
    python \
    build-base \
    python-dev \
    # wget dependency
    openssl \
    # dev dependencies
    git \
    bash \
    sudo \
    py2-pip \
    postgresql-dev

RUN pip install --upgrade pip

RUN mkdir /code
ADD . /code/
WORKDIR /code

RUN pip install -r requirements.txt
