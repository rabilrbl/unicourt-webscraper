FROM python:3.11-alpine
WORKDIR /workspace/site

RUN apk update && \
apk --no-cache add --virtual build-deps-alpine build-base && \
apk --no-cache add --virtual postgresql-deps libpq-dev
# Install requirements
RUN pip install --upgrade pip
RUN pip install Django psycopg2==2.9.3 bs4 html5lib requests

COPY . /workspace/site