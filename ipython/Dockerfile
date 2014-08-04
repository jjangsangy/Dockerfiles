# iPython Notebook
#
# VERSION 0.0.1
#

FROM       jjangsangy/python3:3.4.0
MAINTAINER Sang Han <jjangsangy@gmail.com>

# Enviornment
ENV        HOME       /root
ENV        IPYTHONDIR /root/ipython
ENV        TERM       xterm-256color

WORKDIR    /root/ipython

# Install Ubuntu Packages
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
     gfortran \
     swig \
     python3-matplotlib \
     python3-zmq \
     cython3 \
     libopenblas-dev \
     libatlas-base-dev \
     liblapack-dev \
     libxml2-dev \
     libxslt1-dev \
     python3-numpy \
     python3-scipy \
     ipython3 \
     ipython3-notebook \
     python3-pandas \
     python3-nose \
     pandoc \
 && apt-get autoremove \
 && apt-get clean

# Install Requirements
ADD pip_upgrade /root/ipython/pip_upgrade
RUN pip3 install -U cython \
 && pip3 install -U pyzmq \
 && pip3 install -U ipython[all]
RUN ./pip_upgrade 3

# Configuration
RUN ipython profile create nbserver
ADD profile/ipython_notebook_config.py /root/ipython/profile_nbserver/

VOLUME /root/ipython/notebook
EXPOSE 8080
