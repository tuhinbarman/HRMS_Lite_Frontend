# entrypoint.sh
#!/bin/sh
echo "Waiting for DB..."
while ! nc -z $DB_HOST $DB_PORT; do sleep 1; done
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000