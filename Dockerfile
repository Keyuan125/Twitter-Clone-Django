FROM ubuntu:18.04


# Mount the project directory to the docker containter
ADD ../Twitter-Clone-Django ~/home/Twitter-Clone-Django



RUN apt-get update

RUN apt-get install python3.6

RUN apt-get install tree


RUN dpkg -i mysql-apt-config_0.8.15-1_all.deb
RUN DEBIAN_FRONTEND=noninteractivate apt-get install -y mysql-server
RUN apt-get install -y libmysqlclient-dev

RUN if [ ! -f "/usr/bin/pip" ]; then \
  apt-get install -y python3-pip \
  apt-get install -y python-setuptools \
  ln -s /usr/bin/pip3 /usr/bin/pip
fi

RUN pip install --upgrade setuptools

RUN pip install --ignore-installed wrapt

RUN pip install -U pip

RUN pip install -r requirements.txt

RUN mysql -u root << EOF
	ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
	flush privileges;
	show databases;
	CREATE DATABASE IF NOT EXISTS twitter;
EOF


