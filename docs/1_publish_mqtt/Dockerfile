FROM python:3.8-alpine

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD python mqtt_client_json_publisher.py