# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET


xml_file = 'credentials.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
print('Tree root is %s.' % root.tag)


# for child in root:
#     print(child.tag)

def count_accout(username):
    """
    凭据文件路径：/usr/share/tomcat/.jenkins/credentials.xml，下面就是账号的信息。
    <scope>GLOBAL</scope>
    <id>30b49806-fbec-4dea-99a9-aa3cff0b0492</id>
    <description>github账号</description>
    <username>whh881114@gmail.com</username>
    <password>{AQAAABAAAAAQ/9Gq6yy6GkGd57P8NiVtQRR9EdwZINZNj9WpslWyxpc=}</password>
    """
    sum = 0
    accounts = root.findall('./domainCredentialsMap/entry/java.util.concurrent.CopyOnWriteArrayList/')
    for account in accounts:
        if account[3].text == username:
            sum += 1
            account_uuid = account[2].text

    if sum == 0:
        msg = "输入的用户凭证\"%s\"不存在，请检查。" % (username)
        return False, msg
    elif sum == 1:
        msg = "输入的用户凭证\"%s\"存在且唯一。" % (username)
        return True, msg
    else:
        msg = "输入的用户凭证\"%s\"存在相同的记录，请登录jenkins后台修改凭证使其唯一。" % username
        return False, msg



print('- ' * 50)
username = 'test4'
status, msg = count_accout(username)
if status is False:
    print(msg)

# print('- ' * 50)
# ret = root.findall('./domainCredentialsMap/entry/java.util.concurrent.CopyOnWriteArrayList/')
# for child in ret:
#     print(child[0].text)
#     print(child[1].text)
#     print(child[2].text)
#     print(child[3].text)
#     print(child[4].text)
#     print('* ' * 50)