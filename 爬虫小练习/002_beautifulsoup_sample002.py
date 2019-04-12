# -*- coding: UTF-8 -*-

# 当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。
# 这里的h1就是HTML DOM中的一个节点，换句话说，每个标签都是DOM中的每个节点。


from urllib import urlopen
from bs4 import BeautifulSoup


url = "https://morvanzhou.github.io/static/scraping/list.html"

html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, features="lxml")

print("#####根据class属性进行匹配1：")
month = soup.find_all('li', {"class": "month"})
for m in month:
    # print(type(m), m)
    print(m.get_text())


# 唯一的区别是find_all()方法的返回结果是值包含一个元素的列表，而find()方法直接返回结果。
print("\n")
print("#####根据class属性进行匹配2：")
jan = soup.find('ul', {"class": "jan"})
print(type(jan), jan)

d_jan = jan.find_all("li",)
for d in d_jan:
    print(d)