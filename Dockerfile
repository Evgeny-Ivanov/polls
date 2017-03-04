# Pull base image.
FROM ubuntu:16.04

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y git postgresql postgresql-server-dev-9.5 python3-dev

RUN git clone https://github.com/Evgeny-Ivanov/polls && \
    mkdir polls

WORKDIR polls

RUN pip install -r requirements.txt

CMD ["bash"]
