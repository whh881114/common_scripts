# -*- coding: UTF-8 -*-


# 网页中有中文，需要重装载入sys并设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



from urllib import urlopen
from bs4 import BeautifulSoup
import re
import random
import urllib
import requests


base_url = "https://baike.baidu.com"
his = ["/item/网络爬虫/5162711"]

url = base_url + his[-1]
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')


# 使用这种方式打印结果，会将中文展现出来。
print("%s url: %s" % (soup.find('h1').get_text(), his[-1]))