FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt && pip install django-jquery

COPY . /code/

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

