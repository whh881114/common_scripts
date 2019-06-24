#!/usr/bin/env bash

mkdir -p /var/jenkins_home
chown -R 1000:1000 /var/jenkins_home
docker run --name jenkins -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home -d jenkins



yum -y install java-1.8.0*
wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-9/v9.0.21/bin/apache-tomcat-9.0.21.tar.gz
tar -xf apache-tomcat-9.0.21.tar.gz  -C /usr/local/
cd /usr/local/
ln -s apache-tomcat-9.0.21 tomcat
cd tomcat/webapps
wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war
unzip webapps
cd ../bin/
./catalina.sh start

