FROM python:3.10-slim-buster

WORKDIR /app

#COPY requirements.txt ./
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=/app/index.py flask run --host=0.0.0.0 --port=80