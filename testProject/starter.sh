#!/bin/sh

gunicorn --bind 0.0.0.0:8000 core.wsgi:application &

celery -A core worker --loglevel=info

wait