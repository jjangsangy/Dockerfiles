# Python 3 Base
#
# Python 3.4.1 & pip package manager
# Debian Wheezy
#
# Comes with GNU GCC Compiler and build system used to
# compile Python binaries from source
#
# VERSION 0.0.2

FROM       phusion/baseimage
MAINTAINER Sang Han <jjangsangy@gmail.com>

# Packages
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
     build-essential \
     pkg-config \
     wget \
     git \
     libsqlite3-dev \
     sqlite3 \
     libssl-dev \
     openssl \
     python3-dev \
 && apt-get autoremove \
 && apt-get clean

RUN wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py \
 && python3 get-pip.py \
 && rm -rf get-pip.py

# Python Package Manager
RUN pip3 install -U setuptools \
 && pip3 install -U distribute \
 && pip3 install -U pip \
 && pip3 install -U wheel
