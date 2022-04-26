# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install bs4
RUN pip3 install requests

COPY . .

CMD [ "python3", "main.py"]