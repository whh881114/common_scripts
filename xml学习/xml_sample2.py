# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET


xml_file = 'general_template.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
print('Tree root is %s.' % root.tag)


# print('- ' * 50)
# ret = root.findall('./domainCredentialsMap/entry/java.util.concurrent.CopyOnWriteArrayList/')
# for child in ret:
#     print(child[0].text)
#     print(child[1].text)
#     print(child[2].text)
#     print(child[3].text)
#     print(child[4].text)
#     print('* ' * 50)