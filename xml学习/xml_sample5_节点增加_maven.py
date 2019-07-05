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

builder_node = root.findall("./builders")[0]


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


builder_elem1 = ET.SubElement(builder_node, 'hudson.tasks.Maven')

builder_elem1_1 = ET.SubElement(builder_elem1, 'targets')
builder_elem1_1.text = 'maven测试'

builder_elem1_2 = ET.SubElement(builder_elem1, 'mavenName')
builder_elem1_2.text = 'maven测试2222'

builder_elem1_3 = ET.SubElement(builder_elem1, 'usePrivateRepository')
builder_elem1_3.text = 'false'

builder_elem1_4 = ET.SubElement(builder_elem1, 'settings')
builder_elem1_4.set('class', 'jenkins.mvn.DefaultSettingsProvider')


builder_elem1_5 = ET.SubElement(builder_elem1, 'globalSettings')
builder_elem1_5.set('class', 'jenkins.mvn.DefaultGlobalSettingsProvider')

builder_elem1_6 = ET.SubElement(builder_elem1, 'injectBuildVariables')
builder_elem1_6.text = 'false'


write_xml(root, new_xml_file)