# iPython Notebook
#
# VERSION 0.0.1
#

FROM       jjangsangy/python3:3.4.0
MAINTAINER Sang Han <jjangsangy@gmail.com>

# Enviornment
ENV    HOME       /root
ENV    IPYTHONDIR /root/ipython
ENV    TERM       xterm-256color

WORKDIR /root/ipython

# Install Ubuntu Packages
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
     gfortran \
     swig \
     python3-matplotlib \
     python3-zmq \
     cython3 \
     libblas-dev \
     liblapack-dev \
     libatlas-dev \
     libzmq-dev \
     libxml2-dev \
     libcurl4-openssl-dev \
     libxslt1-dev \
     python3-numpy \
     python3-scipy \
     ipython3 \
     python3-pandas \
     python3-nose \
     pandoc \
 && apt-get autoremove \
 && apt-get clean

# Update Packages and Install Requirements
ADD pip_upgrade /usr/local/bin/
ADD requirements.txt /root/ipython/
RUN pip3 wheel --wheel-dir=/tmp/wheel ipython[all] \
 && pip3 install --use-wheel --no-index --find-links=/tmp/wheel ipython
RUN pip3 install -U ipython[all]

# Configuration
RUN ipython3 profile create nbserver \
 && mkdir -p /etc/service/ipython
ADD service /etc/service
ADD profile_nbserver /root/ipython/profile_nbserver

# Additional Packages
# LLVM 3.3
RUN apt-get install -y python-dev
RUN wget -q -O - http://llvm.org/releases/3.3/llvm-3.3.src.tar.gz \
  | tar xz -C /tmp \
      && cd /tmp/llvm* \
      && ./configure --enable-optimized --prefix=/usr/local \
      && REQUIRES_RTTI=1 make install

# llvmpy
RUN git clone https://github.com/llvmpy/llvmpy \
 && cd llvmpy \
 && LLVM_CONFIG_PATH=/usr/local/bin/llvm-config python3 setup.py install

# numba
RUN git clone https://github.com/numba/numba.git \
 && cd numba \
 && pip3 install -r requirements.txt \
 && python3 setup.py build_ext --inplace \
 && python3 setup.py install

RUN pip3 install -r requirements.txt

WORKDIR /root/notebook
VOLUME /root/notebook
EXPOSE 8888

ADD notebook /root/notebook

# ENTRYPOINT runsvdir-start
# CMD ["/sbin/my_init"]
