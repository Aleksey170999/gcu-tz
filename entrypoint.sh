#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py filldb

python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000
