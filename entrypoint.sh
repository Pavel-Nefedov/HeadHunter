#!/bin/sh

if [ "$DB_TYPE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

make flush
make makemigrations
make migrate
make createsuperuser
make collectstatic

exec "$@"