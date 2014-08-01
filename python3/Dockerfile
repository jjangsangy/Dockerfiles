# Python 3 Base
#
# Python 3.4.1 & pip package manager
# Ubuntu 14.04 LTS Trusty Tahr
#
# Comes with GNU GCC Compiler and build system used to
# compile Python binaries from source
#
# VERSION 0.0.2

FROM       ubuntu:14.04
MAINTAINER Sang Han <jjangsangy@gmail.com>

# Enviornment Variables
ENV  DEBIAN_FRONTEND noninteractive

# Ubuntu Packages
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
 && apt-get autoremove \
 && apt-get clean

# Compile Python
RUN wget -qO- https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz | \
    tar x --xz --directory=/tmp && \
        cd /tmp/Python* && \
            ./configure && \
            make && \
            make install && \
        rm -rf /tmp/*

# Python Package Manager
RUN pip3 install -U setuptools && \
    pip3 install -U distribute && \
    pip3 install -U pip && \
    pip3 install -U wheel
