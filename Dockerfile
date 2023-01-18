# Deriving the base image
FROM python:3.6

# Setting Working Directory
WORKDIR /Twitter-Clone-Django
#
## Copy the entire project folder into working directory
#ADD . /home/Twitter-Clone-Django

RUN python -m pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install mysqlclient
#RUN python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt

#RUN apt-get update
#
#RUN apt-get install python3.6
#
#RUN apt-get install tree
#
#
#RUN dpkg -i mysql-apt-config_0.8.15-1_all.deb
#RUN DEBIAN_FRONTEND=noninteractivate apt-get install -y mysql-server
#RUN apt-get install -y libmysqlclient-dev
#
#RUN if [ ! -f "/usr/bin/pip" ]; then \
#RUN apt-get install -y python3-pip
#RUN apt-get install -y python-setuptools
#  ln -s /usr/bin/pip3 /usr/bin/pip
#fi
#
#RUN pip install --upgrade setuptools
#
#RUN pip install --ignore-installed wrapt
#
#RUN pip install -U pip
##
#RUN pip install -r requirements.txt
#
#RUN mysql -u root << EOF
#	ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
#	flush privileges;
#	show databases;
#	CREATE DATABASE IF NOT EXISTS twitter;
#EOF
#
#
