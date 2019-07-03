# -*- coding: UTF-8 -*-

import jenkins

server = jenkins.Jenkins('http://django2.example.com:8080/jenkins/', username='admin', password='admin')
jobs = server.get_jobs()

# 默认我的任务是不存在的。
job_name = 'empty'
job_name_exist_flag = 0

for job in jobs:
    if job['name'] == job_name:
        job_name_exist_flag = 1
        break

if job_name_exist_flag == 0:
    print('[INFO] %s does not exist then create it.' % job_name)
    server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
else:
    print('[INFO] %s exists and ignore creating job.' % job_name)
    print('[INFO] %s job info:' % job_name)
    print(server.get_job_info(job_name))

print('[INFO] All the jobs:')
print(jobs)

# 获取我的任务xml配置信息。
# job_conf = server.get_job_config('empty')
# print(job_conf)

