FROM debian:latest

RUN apt-get update && \
    apt-get -y install default-mysql-client && \
    apt-get -y install inetutils-ping

EXPOSE 80