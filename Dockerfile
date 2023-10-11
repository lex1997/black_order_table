FROM python:3.11.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client

COPY . /app

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

RUN poetry run python manage.py collectstatic --noinput