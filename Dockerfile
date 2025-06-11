FROM python:3.12-slim-bookworm

MAINTAINER ruicao ruicao@alauda.io

RUN apt-get update

RUN apt-get install -y curl wget

WORKDIR /app

EXPOSE 80

COPY . /app

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
