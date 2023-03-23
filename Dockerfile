FROM python:3.9

ENV APP_HOME /get-kenmo-thread
WORKDIR $APP_HOME
COPY . .

RUN apt-get update && apt-get install
RUN apt-get install -y cmake

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 get-kenmo-thread:app