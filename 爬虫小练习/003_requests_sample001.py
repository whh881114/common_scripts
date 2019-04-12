# -*- coding: UTF-8 -*-


# 网页中有中文，需要重装载入sys并设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import requests
import webbrowser

url = "https://www.baidu.com/s"
param = {"wd": "莫烦Python"}
r = requests.get(url, params=param)
print(r.url)
webbrowser.open(r.url)

