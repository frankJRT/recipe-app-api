FROM python:3.9-buster
MAINTAINER Frank Developer.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y postgresql-client postgresql-server-dev-11
RUN apt-get update && apt-get install -y gcc libc-dev 
RUN apt-get install -y linux-headers-amd64
RUN pip install -r /requirements.txt


# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser user
USER user
