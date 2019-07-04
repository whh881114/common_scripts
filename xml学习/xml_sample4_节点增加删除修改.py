# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom


def write_xml(root, filename, indent="  ", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)



xml_str = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.plugins.git.GitSCM" plugin="git@3.10.0">
    <configVersion>2</configVersion>
    <userRemoteConfigs>
      <hudson.plugins.git.UserRemoteConfig>
        <url>https://github.com/whh881114/mybank-demo-maven.git</url>
        <credentialsId>30b49806-fbec-4dea-99a9-aa3cff0b0492</credentialsId>
      </hudson.plugins.git.UserRemoteConfig>
    </userRemoteConfigs>
    <branches>
      <hudson.plugins.git.BranchSpec>
        <name>*/master</name>
      </hudson.plugins.git.BranchSpec>
    </branches>
    <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
    <submoduleCfg class="list"/>
    <extensions/>
  </scm>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Maven>
      <targets>clean install -D maven.test</targets>
      <mavenName>maven-3.0.5</mavenName>
      <usePrivateRepository>false</usePrivateRepository>
      <settings class="jenkins.mvn.DefaultSettingsProvider"/>
      <globalSettings class="jenkins.mvn.DefaultGlobalSettingsProvider"/>
      <injectBuildVariables>false</injectBuildVariables>
    </hudson.tasks.Maven>
    <hudson.tasks.Shell>
      <command>cp -f /usr/share/tomcat/.jenkins/workspace/java_template/target/ROOT.war /usr/share/tomcat/webapps/mybank-demo.war</command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>"""

origin_xml_file = "origin_xml_file.xml"
new_xml_file = "new_xml_file.xml"

with open(origin_xml_file, 'w') as f:
    f.write(xml_str)



tree = ET.parse(origin_xml_file)
root = tree.getroot()

# 现在要删除builders下的hudson.tasks.Maven。
builders_maven_nodes = root.findall("./builders/hudson.tasks.Shell")
for parent_node in builders_maven_nodes:
    children = parent_node.getchildren()
    for child in children:
            parent_node.remove(child)





tree.write(new_xml_file)




