FROM python:3.9.18-alpine3.18

RUN apk add build-base

RUN apk add postgresql-dev gcc python3-dev musl-dev

ARG FLASK_APP
ARG FLASK_ENV
ARG DATABASE_URL
ARG SCHEMA
ARG SECRET_KEY

ENV DATABASE_URL=sqlite:///dev.db
ENV FLASK_RUN_PORT=8000
ENV FLASK_ENV=development

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY . .

WORKDIR /var/www

RUN flask db upgrade
RUN flask seed all
CMD gunicorn app:app --bind=0.0.0.0
