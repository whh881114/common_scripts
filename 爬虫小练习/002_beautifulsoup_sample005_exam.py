# -*- coding: UTF-8 -*-


# 网页中有中文，需要重装载入sys并设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



from urllib import urlopen
from bs4 import BeautifulSoup
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/网络爬虫/5162711"]

url = base_url + his[-1]
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("(/item/.+$)")})

for i in range(len(sub_urls)):
    # print(type(sub_urls[i]), sub_urls[i])
    print("%-20surl:%s" % (sub_urls[i].string, base_url+sub_urls[i]['href']))



"""
# 查找a标签,只会查找出一个a标签
# print(soup.a)#<a class="sister" href="http://example.com/elsie" id="xiaodeng"><!-- Elsie --></a>

for k in soup.find_all('a'):
    print(k)
    print(k['class'])#查a标签的class属性
    print(k['id'])#查a标签的id值
    print(k['href'])#查a标签的href值
    print(k.string)#查a标签的string
    
# 如果，标签<a>中含有其他标签，比如<em>..</em>，此时要提取<a>中的数据，需要用k.get_text()
--------------------- 
作者：起飞并不晚 
来源：CSDN 
原文：https://blog.csdn.net/slhlde/article/details/81286318 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

