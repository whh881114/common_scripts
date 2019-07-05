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
    <hudson.tasks.Shell>
      <command>cd ${WORKSPACE}
cp -f index.html /var/www/html/index.html
curl http://localhost:8000/index.html</command>
    </hudson.tasks.Shell>
"""


builder_elem1 = ET.SubElement(builder_node, 'hudson.tasks.Shell')

builder_elem1_1 = ET.SubElement(builder_elem1, 'command')
builder_elem1_1.text = """\ncp -f index.html /var/www/html/index.html\n
cp -f index.html /var/www/html/index.html\n
cp -f index.html /var/www/html/index.html"""


write_xml(root, new_xml_file)


