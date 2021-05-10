FROM python:3-slim-buster

WORKDIR /app

RUN pip install prettytable

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

CMD python main.py

COPY . .