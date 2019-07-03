# -*- coding: UTF-8 -*-

import jenkins

server = jenkins.Jenkins('http://django2.example.com:8080/jenkins/', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()

# print('Hello %s from Jenkins %s' % (user['fullName'], version))
#
#
# credentails = server.list_credentials('/usr/share/tomcat/.jenkins/workspace/general_project_template')
# print(credentails)


job_name = 'my_test_demo3'
server.create_job(job_name, jenkins.EMPTY_CONFIG_XML)

