cd /usr/src/app/django_todo
echo "Server started in port $1"
python -m gunicorn --bind :$1 --capture-output --log-file loki.txt todo.wsgi
echo "Bye!"