# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET


xml_file = 'general_template.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
print('Tree root is %s.' % root.tag)