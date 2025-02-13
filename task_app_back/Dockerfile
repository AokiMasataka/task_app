FROM python:3.12.7-bullseye

WORKDIR /app

RUN mkdir /app/task_app

COPY ./task_app /app/task_app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "task_app"]