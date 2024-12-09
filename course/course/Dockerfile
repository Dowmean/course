FROM python:3.11-slim

WORKDIR /myapp

COPY . .

RUN pip install django

RUN python manage.py migrate

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]