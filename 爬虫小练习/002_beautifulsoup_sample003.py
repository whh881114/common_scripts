# -*- coding: UTF-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup
import re


url = "https://morvanzhou.github.io/static/scraping/table.html"

html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, features="lxml")

print("#####找出所有图片地址：")
img_links = soup.find_all("img", {"src": re.compile(".+?\.jpg")})
for img_link in img_links:
    # print(type(img_link), img_link
    # (<class 'bs4.element.Tag'>, <img src="https://morvanzhou.github.io/static/img/course_cover/tf.jpg"/>)
    print(img_link["src"])


print("#####打出所有课程地址：")
course_links = soup.find_all("a", {"href": re.compile("https://morvan.*")})
for course_link in course_links:
    print(course_link['href'])