# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom


def write_xml(root, filename, indent="  ", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)



xml_str = """<project>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class='jenkins.scm.NullSCM'/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers class='vector'/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>"""

origin_xml_file = "origin_xml_file.xml"
new_xml_file = "new_xml_file.xml"

with open(origin_xml_file, 'w') as f:
    f.write(xml_str)



tree = ET.parse(origin_xml_file)
root = tree.getroot()


# 删除了原先的scm节点，针对的是删除一级节点。
scm_nodes = root.findall("./scm")[0]
root.remove(scm_nodes)


# 现在要添加scm节点
"""
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
"""

# 先创建新的元素scm
scm_elem = ET.Element('scm')
root.append(scm_elem)
scm_elem.set("class", "hudson.plugins.git.GitSCM")
scm_elem.set("plugin", "git@3.10.0")

# 然后再创建子元素
scm_sub_elem1 = ET.SubElement(scm_elem, 'configVersion')
scm_sub_elem1.text = '2'

scm_sub_elem2 = ET.SubElement(scm_elem, 'userRemoteConfigs')
scm_sub_elem2_1 = ET.SubElement(scm_sub_elem2, 'hudson.plugins.git.UserRemoteConfig')
scm_sub_elem2_1_1 = ET.SubElement(scm_sub_elem2_1, 'url')
scm_sub_elem2_1_1.text = 'https://github.com/whh881114/mybank-demo-maven.git新的'
scm_sub_elem2_1_2 = ET.SubElement(scm_sub_elem2_1, 'credentialsId')
scm_sub_elem2_1_2.text = '30b49806-fbec-4dea-99a9-aa3cff0b0492新的'

scm_sub_elem3 = ET.SubElement(scm_elem, 'branches')
scm_sub_elem3_1 = ET.SubElement(scm_sub_elem3, 'hudson.plugins.git.BranchSpec')
scm_sub_elem3_1_1 = ET.SubElement(scm_sub_elem3_1, 'name')
scm_sub_elem3_1_1.text = '*/master新的'

scm_sub_elem4 = ET.SubElement(scm_elem, 'doGenerateSubmoduleConfigurations')
scm_sub_elem4.text = 'false'

scm_sub_elem5 = ET.SubElement(scm_elem, 'submoduleCfg')
scm_sub_elem5.set("class", "list")

scm_sub_elem6 = ET.SubElement(scm_elem, 'extensions')



"""
    <hudson.tasks.Maven>
      <targets>clean install -D maven.test</targets>
      <mavenName>maven-3.0.5</mavenName>
      <usePrivateRepository>false</usePrivateRepository>
      <settings class="jenkins.mvn.DefaultSettingsProvider"/>
      <globalSettings class="jenkins.mvn.DefaultGlobalSettingsProvider"/>
      <injectBuildVariables>false</injectBuildVariables>
    </hudson.tasks.Maven>
"""

write_xml(root, new_xml_file)


