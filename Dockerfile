FROM python:3.12-alpine

WORKDIR /app

RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main curl

RUN apk update && apk add --no-cache --virtual bash c-ares git gcc g++

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
