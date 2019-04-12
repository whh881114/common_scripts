# -*- coding: UTF-8 -*-

# 当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。
# 这里的h1就是HTML DOM中的一个节点，换句话说，每个标签都是DOM中的每个节点。


from urllib import urlopen
from bs4 import BeautifulSoup


url = "https://morvanzhou.github.io/static/scraping/basic-structure.html"

html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, features="lxml")

print("#####使用urlopen打开网页后，然后将html内容放入BeautifulSoup中进行lxml解析。\n")

print("#####打印h1标签内容（只匹配第一个h1标签）：\n")
print(soup.h1)

print("\n#####打印p标签内容（只匹配第一个p标签）：\n")
print(soup.p)


print("\n#####打印所有a标签内容：\n")
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]    # 漂亮的写法。
print(all_href)
