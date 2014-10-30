# ownCloud Server 7
#
# VERSION 0.0.1
FROM       phusion/baseimage:latest
MAINTAINER Sang Han <jjangsangy@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
RUN apt-get update && apt-get upgrade -y

# Build nginx
RUN apt-get install -y wget nginx php5-common php5-cli php5-fpm openssl
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

# Configure
ADD owncloud_nginx.conf /etc/nginx/sites-available/owncloud

# PHP
RUN apt-get install -y php5-fpm php5-mysql php-apc php5-imagick php5-imap php5-mcrypt
RUN apt-get install -y php5-intl php5-mcrypt php5-imagick
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf

# Configure SQL

# Get Owncloud
RUN mkdir /var/www
RUN wget -q -O - https://download.owncloud.org/community/owncloud-7.0.0.tar.bz2 | tar jx -C /var/www
RUN chown -R www-data: /var/www/owncloud

CMD service php5-fpm start && nginx
ENV DEBIAN_FRONTEND dialog
VOLUME ["/var/www/owncloud/data"]
EXPOSE 80
EXPOSE 443
