# -*- coding: UTF-8 -*-

import jenkins

server = jenkins.Jenkins('http://192.168.255.229:8080/jenkins/', username='admin', password='admin')

# 测试验证信息，打印jenkins主机的url。
print(server.server)

server.get_all_jobs()
