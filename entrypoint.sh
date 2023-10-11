#!/bin/sh

python manage.py makemigrations web
python manage.py migrate
python manage.py populate_data

exec "$@"