# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET


xml_file = 'hudson.tasks.Maven.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
mavens = root.findall('./installations/hudson.tasks.Maven_-MavenInstallation/name')
for maven in mavens:
    print(type(maven), maven, maven.text)