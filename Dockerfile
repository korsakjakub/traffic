FROM python:3.10-slim-buster

WORKDIR /app

RUN useradd -ms /bin/bash user
USER user
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
