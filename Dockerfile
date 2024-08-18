FROM python:3.12.2-bookworm

COPY ./src /app
COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

CMD [ "python", "/app/main.py" ]

