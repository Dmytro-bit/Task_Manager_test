#!/bin/bash

set -e
chmod +x wait-for-it.sh
./wait-for-it.sh postgres-db:5432 --timeout=5 --strict -- \
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn Task_Manager.wsgi:application --bind 0.0.0.0:8000