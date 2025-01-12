cd /usr/src/app/django_todo
python manage.py migrate
python shutdown_watchdog.py &
echo "Server started in port $1"
python -m gunicorn --bind :$1 --env IN_CONTAINER=$2 todo.wsgi
echo "Bye!"