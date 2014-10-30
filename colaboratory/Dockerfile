# iPython Notebook
# Jupyter CoLaboratory
#
# VERSION 0.0.1
#
# Based off phusion ubuntu base image
# https://github.com/phusion/baseimage-docker

FROM       phusion/baseimage:latest
MAINTAINER Sang Han <jjangsangy@gmail.com>

# Enviornment
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
ENV IPYTHONDIR $HOME/ipython
ENV LANG en_US.UTF-8
WORKDIR /root

# Google Chrome PPA
RUN curl "https://dl-ssl.google.com/linux/linux_signing_key.pub" | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get upgrade -y

# Ubuntu Packages
RUN apt-get install -y git wget openssh-server libsqlite3-dev sqlite3
RUN apt-get install -y build-essential gfortran swig
RUN apt-get install -y lxde-core lxterminal tightvncserver google-chrome-beta
RUN apt-get install -y python-software-properties python-dev python-pip pkg-config
RUN apt-get install -y python-matplotlib

# Install Statistical Packages
RUN apt-get install -y liblapack-dev libatlas-dev libffi-dev libblas3gf liblapack3gf
RUN apt-get install -y libatlas-base-dev libatlas-dev libatlas-doc libatlas-test libatlas3gf-base

#0MQ
RUN wget -q -O - http://download.zeromq.org/zeromq-3.2.4.tar.gz | tar xvz -C /tmp
RUN cd /tmp/zeromq* && ./configure && make install

# Python Packages
RUN pip install -U setuptools \
 && pip install -U distribute \
 && pip install -U wheel
RUN pip install -U pip
RUN pip install cython

# Install Requirements
ADD requirements.txt .
RUN pip install -r requirements.txt

# Install IPython
RUN pip install ipython[all]

# Build CoLaboratory
RUN git clone --recursive https://github.com/jupyter/colaboratory.git
RUN python colaboratory/install_chrome.py --release
RUN google-chrome --load-extension chrome-build

RUN ipython profile create nbserver
ADD conf/ipython_notebook_config.py /root/ipython/profile_nbserver/ipython_notebook_config.py

EXPOSE 8080

VOLUME /root/ipython/notebook
WORKDIR /root/ipython/notebook

ENTRYPOINT ["ipython", "notebook"]

CMD ["--BaseIPythonApplication.profile=nbserver"]
