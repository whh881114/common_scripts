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

# 删除了原先的scm节点
scm_node = root.findall("./scm")[0]
root.remove(scm_node)
tree.write(new_xml_file)

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

# 然后再创建子元素
scm_sub_elem1 = ET.SubElement(scm_elem, 'configVersion')
scm_sub_elem1.text = '2'

scm_sub_elem2 = ET.SubElement(scm_elem, 'userRemoteConfigs')
scm_sub_elem3 = ET.SubElement(scm_sub_elem2, 'hudson.plugins.git.UserRemoteConfig')
scm_sub_elem4 = ET.SubElement(scm_sub_elem3, 'url')
scm_sub_elem4.text = 'https://github.com/whh881114/mybank-demo-maven.git'
scm_sub_elem4 = ET.SubElement(scm_sub_elem3, 'credentialsId')
scm_sub_elem4.text = '30b49806-fbec-4dea-99a9-aa3cff0b0492'


write_xml(root, new_xml_file)


