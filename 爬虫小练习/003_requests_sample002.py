# -*- coding: UTF-8 -*-


# 网页中有中文，需要重装载入sys并设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import requests


url = "http://pythonscraping.com/files/form.html"
data = "{'firstname': '浩浩', 'lastname': '汪'}"
r = requests.post(url, data=data)   # 需要注意地方：data传入时，写的内容是表单里的，而json参数是是在请求体中，web界面上是没有表单的。
print(r.text)


data = {'firstname': '浩浩', 'lastname': '汪'}
url = "http://pythonscraping.com/files/processing.php"
r = requests.post(url, data=data)
print(r.text)



# requests包，就是来做高级操作：如用户登录，然后获取Cookie信息，除了这个一般也不会搞点别的了，毕竟只是去抓数据而已。


"""
在通过requests.post()进行POST请求时，传入报文的参数有两个，一个是data，一个是json。

data与json既可以是str类型，也可以是dict类型。

区别：

1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json

2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式

3、data为str时，如果不指定content-type，默认为application/json

4、用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式

出处：https://www.cnblogs.com/yanlin-10/p/9820694.html
"""
