# -*- coding: UTF-8 -*-

import jenkins

server = jenkins.Jenkins('http://django2.example.com:8080/jenkins/', username='admin', password='admin')

# 使用reconf_view去修改jobNames节点，把新建的job写入进去即可。
"""
>>> print(server.get_view_config('member'))
<?xml version="1.1" encoding="UTF-8"?>
<hudson.model.ListView>
  <name>member</name>
  <filterExecutors>false</filterExecutors>
  <filterQueue>false</filterQueue>
  <properties class="hudson.model.View$PropertyList"/>
  <jobNames>
    <comparator class="hudson.util.CaseInsensitiveComparator"/>
    <string>uniseq-member-tomcat-core</string>
  </jobNames>
  <jobFilters/>
  <columns>
    <hudson.views.StatusColumn/>
    <hudson.views.WeatherColumn/>
    <hudson.views.JobColumn/>
    <hudson.views.LastSuccessColumn/>
    <hudson.views.LastFailureColumn/>
    <hudson.views.LastDurationColumn/>
    <hudson.views.BuildButtonColumn/>
  </columns>
  <recurse>false</recurse>
</hudson.model.ListView>
>>> 
"""


