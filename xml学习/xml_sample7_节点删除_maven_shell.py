# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom
import subprocess

def write_xml(root, filename, indent="  ", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)

def delete_sub_node(sub_node):
    sub_nodes = root.findall(sub_node)
    for parent_node in sub_nodes:
        children = parent_node.getchildren()
        for child in children:
            parent_node.remove(child)

origin_xml_file = "java_template.xml"
new_xml_file = 'java_template_deleted_maven.xml'
tree = ET.parse(origin_xml_file)
root = tree.getroot()

delete_sub_node("./builders/hudson.tasks.Maven")

write_xml(root, new_xml_file)
subprocess.call("sed -i 's/\ *$//g' %s" % new_xml_file, shell=True)
subprocess.call("sed -i '/^$/d' %s" % new_xml_file, shell=True)


