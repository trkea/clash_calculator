kill -9 `lsof -ti tcp:8000`
python manage.py runserver
