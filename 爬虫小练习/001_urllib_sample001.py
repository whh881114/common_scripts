# -*- coding: UTF-8 -*-

from urllib import urlopen
import re


url = "https://morvanzhou.github.io/static/scraping/basic-structure.html"

html = urlopen(url).read().decode("utf-8")
print("- " * 80)
print("#####网页原始内容: ")
print(html)
print("- " * 80)
print("\n")


res = re.findall("<title>(.+?)</title>", html)
print("#####使用正则匹配标题的内容：")
print(res[0])
print("- " * 80)
print("\n")


res = re.findall("<p>(.+?)</p>", html, flags=re.DOTALL)
print("#####使用正则匹配的<p>标签内容，只显示第一个<p>标签内容：")
print(res[0])
print("- " * 80)
print("\n")


res = re.findall("href=\"(.+?)\"", html)
print("#####使用正则匹配所有链接地址，内容如下：")
print(res)
print("- " * 80)
print("\n")