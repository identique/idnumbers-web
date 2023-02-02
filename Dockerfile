FROM python:3.10.3-slim

ENV SERVER_PORT=8000
ENV APP_HOME_DIR=/app

WORKDIR ${APP_HOME_DIR}
COPY ./app ./app
COPY ./requirements/requirements-prod.txt ./requirements-prod.txt
COPY ./scripts/run_docker.sh ./run_docker.sh

RUN chmod +x $APP_HOME_DIR/run_docker.sh

RUN apt update
RUN pip3 install -U pip
RUN pip3 install -r requirements-prod.txt

CMD uvicorn app.main:app --host 0.0.0.0 --port $SERVER_PORT
