#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2018/1/17


import jenkins

server = jenkins.Jenkins('http://127.0.0.1:8080', username="admin", password="admin123")
params = {'Branch': 'oriin/master', 'host': '192.168.1.110'}

# server对象
# Jenkins的job数量
print(server.jobs_count())
'''
2
'''

# Jenkins-web-ui
print(server.server)
'''
http://127.0.0.1:8080/
'''

# 所有的job信息
all_jobs_li = server.get_all_jobs()
for item in all_jobs_li:
    print('name: %s' % item['name'], 'URL: ', item['url'])
'''
name: ansible-playbook URL:  http://127.0.0.1:8080/job/ansible-playbook/
name: my-github URL:  http://127.0.0.1:8080/job/my-github/
'''

# 账户信息描述
print(server.get_whoami())
'''
{'_class': 'hudson.model.User', 'absoluteUrl': 'http://127.0.0.1:8080/user/admin', 'description': '本地测试', 'fullName': '管理员', 'id': 'admin', 'property': [{'_class': 'jenkins.security.ApiTokenProperty'}, {'_class': 'com.cloudbees.plugins.credentials.UserCredentialsProvider$UserCredentialsProperty'}, {'_class': 'hudson.tasks.Mailer$UserProperty', 'address': 'admin@163.com'}, {'_class': 'hudson.plugins.emailext.watching.EmailExtWatchAction$UserProperty', 'triggers': []}, {'_class': 'jenkins.security.LastGrantedAuthoritiesProperty'}, {'_class': 'org.jenkinsci.plugins.displayurlapi.user.PreferredProviderUserProperty'}, {'_class': 'hudson.model.PaneStatusProperties'}, {'_class': 'org.jenkinsci.main.modules.cli.auth.ssh.UserPropertyImpl'}, {'_class': 'hudson.security.HudsonPrivateSecurityRealm$Details'}, {'_class': 'hudson.model.MyViewsProperty'}, {'_class': 'hudson.search.UserSearchProperty', 'insensitiveSearch': True}, {'_class': 'hudson.plugins.favorite.user.FavoriteUserProperty'}]}
'''

# auth
print(server.auth)
'''
b'Basic YWRtaW46YWRtaW4xMjM='
'''

# DEBUG Job信息
print(server.debug_job_info('ansible-playbook'))
'''
_class hudson.model.FreeStyleProject
actions [{'_class': 'hudson.model.ParametersDefinitionProperty', 'parameterDefinitions': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition', 'defaultParameterValue': None, 'description': '分支', 'name': 'Branch', 'type': 'PT_BRANCH'}, {'_class': 'hudson.model.StringParameterDefinition', 'defaultParameterValue': {'_class': 'hudson.model.StringParameterValue', 'value': '127.0.0.1,127.0.0.2,127.0.0.1'}, 'description': '本机', 'name': 'host', 'type': 'StringParameterDefinition'}]}, {}, {}, {}, {}, {'_class': 'com.cloudbees.plugins.credentials.ViewCredentialsAction'}]
description ansible playbook
displayName ansible-playbook
displayNameOrNull None
fullDisplayName ansible-playbook
fullName ansible-playbook
name ansible-playbook
url http://127.0.0.1:8080/job/ansible-playbook/
buildable True
......
'''

####### CURD Job #######

# Job是否存在
print(server.job_exists('my-api'))
'''
True or None
'''

# 获取所有的Job
print(server.get_jobs())
'''
[{'_class': 'hudson.model.FreeStyleProject', 'name': 'ansible-playbook', 'url': 'http://127.0.0.1:8080/job/ansible-playbook/', 'color': 'aborted', 'fullname': 'ansible-playbook'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'my-api', 'url': 'http://127.0.0.1:8080/job/my-api/', 'color': 'notbuilt', 'fullname': 'my-api'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'my-github', 'url': 'http://127.0.0.1:8080/job/my-github/', 'color': 'disabled', 'fullname': 'my-github'}]
'''

# 创建Job
server.create_job('API', jenkins.RECONFIG_XML)

# 删除Job
server.delete_job('my-api')

# 复制job
server.copy_job('my-github', 'copy-my-github')

# enable job
server.enable_job('copy-my-github')

# 禁用Job
server.disable_job('copy-my-github')

# 重新配置Job
server.reconfig_job('copy-my-github', jenkins.RECONFIG_XML)

# 重命名Job
server.rename_job('API', 'my-api')

# 触发Job运行
# 触发Job(方式一)
server.build_job_url('ansible-playbook', parameters=params)
'''
http://127.0.0.1:8080/job/ansible-playbook/buildWithParameters?Branch=oriin%2Fmaster&host=192.168.1.110
'''
# 触发Job(方式二)
server.build_job('ansible-playbook', parameters=params)

# 查看指定构建编号的输出
print(server.get_build_console_output('ansible-playbook', 41))
'''
Started by user 管理员
[EnvInject] - Loading node environment variables.
Building in workspace /Users/zhao/data/workspace/workspace/ansible-playbook
 > /usr/local/bin/git rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > /usr/local/bin/git config remote.origin.url git@git.icbc.net:ansible-roles/zff.ansible.git # timeout=10
Fetching upstream changes from git@git.icbc.net:ansible-roles/zff.ansible.git
 > /usr/local/bin/git --version # timeout=10
using GIT_SSH to set credentials deploy key
 > /usr/local/bin/git fetch --tags --progress git@git.icbc.net:ansible-roles/zff.ansible.git +refs/heads/*:refs/remotes/origin/*
 > /usr/local/bin/git rev-parse refs/remotes/origin/master^{commit} # timeout=10
 > /usr/local/bin/git rev-parse refs/remotes/origin/origin/master^{commit} # timeout=10
Checking out Revision 21c2b6ff6c842a86969f36f75424e17ae27eae68 (refs/remotes/origin/master)
 > /usr/local/bin/git config core.sparsecheckout # timeout=10
 > /usr/local/bin/git checkout -f 21c2b6ff6c842a86969f36f75424e17ae27eae68
Commit message: "update tomcat root mode"
 > /usr/local/bin/git rev-list --no-walk 21c2b6ff6c842a86969f36f75424e17ae27eae68 # timeout=10
[ansible-playbook] $ /bin/sh -xe /Users/Shared/Jenkins/tmp/jenkins5080034200775659821.sh
+ echo 192.168.1.110
192.168.1.110
+ echo test
test
+ echo http://127.0.0.1:8080/job/ansible-playbook/41/
http://127.0.0.1:8080/job/ansible-playbook/41/
+ echo 41
41
+ echo jenkins-ansible-playbook-41
jenkins-ansible-playbook-41
Finished: SUCCESS
'''

# 下一次构建编号,步长为5
next_bn = server.get_job_info('ansible-playbook')['nextBuildNumber']
server.set_next_build_number('ansible-playbook', next_bn + 5)

# 指定编号的构建Job信息
print(server.get_build_info('ansible-playbook', 48))
'''
{'_class': 'hudson.model.FreeStyleBuild', 'actions': [{'_class': 'hudson.model.ParametersAction', 'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue', 'name': 'Branch', 'value': 'oriin/master'}, {'_class': 'hudson.model.StringParameterValue', 'name': 'host', 'value': '192.168.1.110'}]}, {'_class': 'hudson.model.CauseAction', 'causes': [{'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user 管理员', 'userId': 'admin', 'userName': '管理员'}]}, {}, {'_class': 'hudson.plugins.git.util.BuildData', 'buildsByBranchName': {'refs/remotes/origin/master': {'_class': 'hudson.plugins.git.util.Build', 'buildNumber': 48, 'buildResult': None, 'marked': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}, 'revision': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}}}, 'lastBuiltRevision': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}, 'remoteUrls': ['git@git.icbc.net:ansible-roles/zff.ansible.git'], 'scmName': ''}, {'_class': 'hudson.plugins.git.GitTagAction'}, {}, {}, {}, {}], 'artifacts': [], 'building': False, 'description': None, 'displayName': '#48', 'duration': 1861, 'estimatedDuration': 4305, 'executor': None, 'fullDisplayName': 'ansible-playbook #48', 'id': '48', 'keepLog': False, 'number': 48, 'queueId': 24, 'result': 'SUCCESS', 'timestamp': 1516185645519, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/48/', 'builtOn': '', 'changeSet': {'_class': 'hudson.plugins.git.GitChangeSetList', 'items': [], 'kind': 'git'}, 'culprits': []}
'''

# 获取正在运行的Job，一般结合build_job方法一起使用
print(server.get_running_builds())
'''
[{'name': 'ansible-playbook', 'number': 57, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/57/', 'node': '(master)', 'executor': 1}]
'''

# 终止指定编号的Job
server.stop_build('ansible-playbook', 62)

# 获取Job名称
print(server.get_job_name('ansible-playbook'))
'''
ansible-playbook
'''

# 断言Job是否存在
print(server.assert_job_exists('ansible-playbook'))
'''
存在则返回None，不存在则抛出错误信息
'''

# 该Job所有的相关信息
print(server.get_job_info('ansible-playbook'))
'''
{'_class': 'hudson.model.FreeStyleProject', 'actions': [{'_class': 'hudson.model.ParametersDefinitionProperty', 'parameterDefinitions': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition', 'defaultParameterValue': None, 'description': '分支', 'name': 'Branch', 'type': 'PT_BRANCH'}, {'_class': 'hudson.model.StringParameterDefinition', 'defaultParameterValue': {'_class': 'hudson.model.StringParameterValue', 'value': '127.0.0.1,127.0.0.2,127.0.0.1'}, 'description': '本机', 'name': 'host', 'type': 'StringParameterDefinition'}]}, {}, {}, {}, {}, {}, {'_class': 'com.cloudbees.plugins.credentials.ViewCredentialsAction'}], 'description': 'ansible playbook', 'displayName': 'ansible-playbook', 'displayNameOrNull': None, 'fullDisplayName': 'ansible-playbook', 'fullName': 'ansible-playbook', 'name': 'ansible-playbook', 'url': 'http://127.0.0.1:8080/job/ansible-playbook/', 'buildable': True, 'builds': [{'_class': 'hudson.model.FreeStyleBuild', 'number': 62, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/62/'}, {'_class': 'hudson.model.FreeStyleBuild', 'number': 61, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/61/'}, {'_class': 'hudson.model.FreeStyleBuild', 'number': 60, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/60/'}, {'_class': 'hudson.model.FreeStyleBuild', 'number': 59, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/59/'}, {'_class': 'hudson.model.FreeStyleBuild', 'number': 58, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/58/'}], 'color': 'aborted', 'firstBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 58, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/58/'}, 'healthReport': [{'description': 'Build stability: No recent builds failed.', 'iconClassName': 'icon-health-80plus', 'iconUrl': 'health-80plus.png', 'score': 100}], 'inQueue': False, 'keepDependencies': False, 'lastBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 62, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/62/'}, 'lastCompletedBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 62, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/62/'}, 'lastFailedBuild': None, 'lastStableBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 61, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/61/'}, 'lastSuccessfulBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 61, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/61/'}, 'lastUnstableBuild': None, 'lastUnsuccessfulBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 62, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/62/'}, 'nextBuildNumber': 63, 'property': [{'_class': 'jenkins.model.BuildDiscarderProperty'}, {'_class': 'hudson.model.ParametersDefinitionProperty', 'parameterDefinitions': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition', 'defaultParameterValue': None, 'description': '分支', 'name': 'Branch', 'type': 'PT_BRANCH'}, {'_class': 'hudson.model.StringParameterDefinition', 'defaultParameterValue': {'_class': 'hudson.model.StringParameterValue', 'name': 'host', 'value': '127.0.0.1,127.0.0.2,127.0.0.1'}, 'description': '本机', 'name': 'host', 'type': 'StringParameterDefinition'}]}], 'queueItem': None, 'concurrentBuild': False, 'downstreamProjects': [], 'labelExpression': None, 'scm': {'_class': 'hudson.plugins.git.GitSCM'}, 'upstreamProjects': []}
'''

# 查看该试图下所有的Job
print(server.get_jobs('myview'))
'''
[{'_class': 'hudson.model.FreeStyleProject', 'name': 'ansible-playbook', 'url': 'http://127.0.0.1:8080/job/ansible-playbook/', 'color': 'aborted', 'fullname': 'ansible-playbook'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'my-api', 'url': 'http://127.0.0.1:8080/job/my-api/', 'color': 'notbuilt', 'fullname': 'my-api'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'my-github', 'url': 'http://127.0.0.1:8080/job/my-github/', 'color': 'disabled', 'fullname': 'my-github'}]
'''

# 正则匹配获取Job信息
# print(server.get_job_info_regex('^my'))
'''
Job相关信息
....
'''

# 获取最后一次构建的Job信息
# build a parameterized job
# requires creating and configuring the ansible-playbook job to accept 'param1' & 'param2'
job_name = "ansible-playbook"
server.build_job(job_name, {'Branch': 'oriin/master', 'host': '192.168.1.110'})
last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
build_info = server.get_build_info(job_name, last_build_number)
print(build_info)
'''
{'_class': 'hudson.model.FreeStyleBuild', 'actions': [{'_class': 'hudson.model.ParametersAction', 'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue', 'name': 'Branch', 'value': 'origin/master'}, {'_class': 'hudson.model.StringParameterValue', 'name': 'host', 'value': '127.0.0.1,127.0.0.2,127.0.0.105'}]}, {'_class': 'hudson.model.CauseAction', 'causes': [{'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user 管理员', 'userId': 'admin', 'userName': '管理员'}]}, {}, {'_class': 'hudson.plugins.git.util.BuildData', 'buildsByBranchName': {'refs/remotes/origin/master': {'_class': 'hudson.plugins.git.util.Build', 'buildNumber': 62, 'buildResult': None, 'marked': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}, 'revision': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}}}, 'lastBuiltRevision': {'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'branch': [{'SHA1': '21c2b6ff6c842a86969f36f75424e17ae27eae68', 'name': 'refs/remotes/origin/master'}]}, 'remoteUrls': ['git@git.icbc.net:ansible-roles/zff.ansible.git'], 'scmName': ''}, {'_class': 'hudson.plugins.git.GitTagAction'}, {}, {'_class': 'jenkins.model.InterruptedBuildAction'}, {}, {}, {}], 'artifacts': [], 'building': False, 'description': None, 'displayName': '#62', 'duration': 7069, 'estimatedDuration': 7681, 'executor': None, 'fullDisplayName': 'ansible-playbook #62', 'id': '62', 'keepLog': False, 'number': 62, 'queueId': 33, 'result': 'ABORTED', 'timestamp': 1516186369042, 'url': 'http://127.0.0.1:8080/job/ansible-playbook/62/', 'builtOn': '', 'changeSet': {'_class': 'hudson.plugins.git.GitChangeSetList', 'items': [], 'kind': 'git'}, 'culprits': []}
'''

# shutdown jenkins
server.quiet_down()