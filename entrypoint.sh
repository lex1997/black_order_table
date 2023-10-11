#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py populate_data

exec "$@"