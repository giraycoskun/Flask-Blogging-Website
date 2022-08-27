FROM python:3.10.6-slim-buster

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY  ./src .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app