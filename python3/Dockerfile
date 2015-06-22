# Python 3 Base
#
# Python 3.4.3
# Continuum Anacondas Python Distribution
# Debian Wheezy
#
# Comes with GNU GCC Compiler and build system used to
# compile Python binaries from source
#
FROM debian:wheezy

MAINTAINER Sang Han <jjangsangy@gmail.com>

# Environment Variables
ENV PYTHONINTERP    3
ENV CONDA_VERSION   2.2.0
ENV DEBIAN_FRONTEND noninteractive
ENV INSTALLER       Anaconda${PYTHONINTERP}-${CONDA_VERSION}-Linux-x86_64.sh
ENV LINK            http://repo.continuum.io/archive/${INSTALLER}

# Working in Root for Now
WORKDIR /root/
COPY bin/ src/ ./

RUN apt-get update && \
    apt-get install -y bzip2 ca-certificates curl && \
    apt-get autoremove && \
    apt-get clean && \
    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    PATH=/opt/conda/bin:$PATH  && ./get_anaconda.sh  && \
    conda update -p /opt/conda -y conda && \
    conda clean  -y --lock     \
                    --tarballs  \
                    --packages   \
                    --index-cache \
                    --source-cache

ENV PATH "/opt/conda/bin:$PATH"
