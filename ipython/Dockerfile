# iPython Notebook
#
# VERSION 0.0.1
#
FROM jjangsangy/python3

MAINTAINER Sang Han <jjangsangy@gmail.com>

LABEL ipython.version=3.0.1

ENV LANG C.UTF-8
ENV TERM xterm-256color

RUN useradd \
    --create-home \
    --home-dir /home/condauser \
    --shell /bin/bash condauser

# Setup Environment
WORKDIR   /home/condauser
EXPOSE    8888
USER      condauser
ENV USER  condauser
ENV HOME  /home/condauser
ENV SHELL /bin/bash

VOLUME ["notebooks"]

ENTRYPOINT ["ipython", "notebook"]
