# Python 3 Base
#
# Python 3.4.1 & pip package manager
# Debian Wheezy
#
# Comes with GNU GCC Compiler and build system used to
# compile Python binaries from source
#
FROM debian:wheezy

MAINTAINER Sang Han <jjangsangy@gmail.com>

# Environment Variables
ENV LANG          C.UTF-8
ENV PYTHONINTERP  3
ENV CONDA_VERSION 2.2.0
ENV TERM          xterm-256color
ENV INSTALLER     Anaconda${PYTHONINTERP}-${CONDA_VERSION}-Linux-x86_64.sh
ENV LINK          http://repo.continuum.io/archive/${INSTALLER}

# Create User
RUN useradd --create-home --home-dir /home/condauser --shell /bin/bash condauser
WORKDIR /home/condauser

# System Packages
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y \
        bzip2 \
        ca-certificates \
        curl \
    && apt-get autoremove \
    && apt-get clean

# Install Anaconda
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh
COPY ./src/* ./src/
COPY ./bin/get_anaconda.sh get_anaconda.sh

RUN ./get_anaconda.sh

ENV PATH "/opt/conda/bin:$PATH"

RUN conda update -p /opt/conda -y conda \
    && conda clean -y --lock --tarballs --index-cache --packages --source-cache

# Setup Environment
EXPOSE 8888
USER condauser
ENV HOME=/home/condauser
ENV SHELL=/bin/bash
ENV USER=condauser

