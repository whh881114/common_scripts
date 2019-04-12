# -*- coding: UTF-8 -*-

"""
BBC LEARNING ENGLISH 是一个很好的网站，希望热爱学习英语的小伙伴去看看这个网站。（友情提示：需要翻墙。）
6-MINUTE-ENGLISH 是一周推出一个话题，内容与时俱进，难度适中。

爬虫目标：下载每个topic的图片，标题，时间，简介，pdf文档以及mp3。

备注：2014年9月前的学习资料已归，内容还是很多的从2008年就有了，
地址为：http://www.bbc.co.uk/worldservice/learningenglish/general/sixminute/，但是我们只抓主页上的内容。

主页：http://www.bbc.co.uk/learningenglish/english/features/6-minute-english

时间：2019-04-12
"""


# 网页中有中文，需要重装载入sys并设置编码为utf-8，虽然这个网站是全英文的，但是还是使用这个设置，毕竟通用。
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import os
import subprocess

# 第一步：定义最基本信息，网站不需要登录，只需要使用到最基本的GET操作。
base_url = "http://www.bbc.co.uk"
index_url = "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english"


# 冰冷事实，国内现在无法使用curl访问的，只好使用国外VPS。大概两三年前是可以的，我当时使用perl做正则匹配，然后生成url进行下载PDF。
try:
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    r = s.get(index_url, timeout=5)
except requests.exceptions.ConnectionError as e:
    print("原始错误信息：%s\n" % e)
    print("简洁错误信息：连接网站(%s)超时，现退出。" % index_url)
    sys.exit(255)

html = r.text.decode("utf-8")
soup = BeautifulSoup(html, features="lxml")


# 第二步：分析网页规则，找出所需要的信息。这个就是我需要的信息，例子如下。
"""
<div class="text">
	<h2><a  href="/learningenglish/english/features/6-minute-english/ep-190404">Why do we feel awkward?</a></h2>
	<div class="details">
		<h3>
																<b>Episode 190404 </b>

				 / 				  04 Apr 2019						</h3>
		<p>Do you know that cringey feeling?</p>
	</div>
</div>

# 每个episode所需要的信息：
# ep_url: http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-190404
# ep_date: Episode 190404 / 04 Apr 2019
# ep_brief: Do you know that cringey feeling?
# ep_img_url: http://ichef.bbci.co.uk/images/ic/1920xn/p070rp20.jpg
# ep_pdf_url: http://downloads.bbc.co.uk/learningenglish/features/6min/190404_6min_awkward.pdf
# ep_mp3_url: http://downloads.bbc.co.uk/learningenglish/features/6min/190404_6min_awkward_download.mp3
"""


# ep_list用于存放所有episode信息的列表，ep_element则存放每个episode的元信息。
ep_list = []

ep_text = soup.find_all('div', {"class": "text"})
for ep in ep_text:
    ep_element = {
        "ep_url": "",
        "ep_date": "",
        "ep_title": "",
        "ep_brief": "",
        "ep_img_url": "",
        "ep_pdf_url": "",
        "ep_mp3_url": ""
    }

    # 初始化变量
    ep_url = ""
    ep_date = ""
    ep_title = ""
    ep_brief = ""
    ep_img_url = ""
    ep_pdf_url = ""
    ep_mp3_url = ""

    # 第一步：获取url信息，可以从里面取到标题，还在地址。
    # 使用正则匹配，是为了排除这个归档url: http://www.bbc.co.uk/worldservice/learningenglish/general/sixminute/。
    url = ep.find("a", {'href': re.compile('/learningenglish/english/features/6-minute-english/.+')})

    # print(type(url), url)
    # (<class 'bs4.element.ResultSet'>,
    # <a href="/learningenglish/english/features/6-minute-english/ep-190404">Why do we feel awkward?</a>)

    if url is None:
        pass
    else:
        ep_title = url.string
        ep_url = base_url + url['href']

    ep_element['ep_title'] = ep_title
    ep_element['ep_url'] = ep_url


    # 第二步：获取到episode的日期。
    details = ep.find('div', {"class": "details"})
    if details is None:
        pass
    else:
        # print(type(details.h3), details.h3)
        # print(type(details.p), details.p)
        # (<class 'bs4.element.Tag'>, <h3>\n<b> Episode 190404 </b> \n\t\t\t\t\t\t\t \n\t\t\t\t /  \t\t\t\t  04 Apr 2019\t\t\t\t\t\t </h3>)
        # (<class 'bs4.element.Tag'>, <p>Do you know that cringey feeling?</p>)

        tmp = str(details.h3)
        tmp = tmp.replace("\n", "")
        tmp = tmp.replace("\t", "")

        episode_sn = re.findall("<b>(.*)</b>", tmp)[0].strip(' ')
        episode_date = re.findall("</b>(.*)</h3>", tmp)[0].strip(' ')
        ep_element['ep_date'] = episode_sn + " " + episode_date

        # 第三步：获取episode的简短介绍。
        tmp = str(details.p)
        tmp = tmp.replace("<p>", "")
        tmp = tmp.replace("</p>", "")
        tmp = tmp.replace("\n", "")
        ep_element['ep_brief'] = tmp

    # 至此，在text这个div中已经取完了所有信息。
    ep_list.append(ep_element)


# 第三步：还需要在主页中，查找episode所对应的图片地址，因为跳转后，图片已变成了视频。
img_divs = soup.find_all('div', {"class": "img"})
for img_div in img_divs:
    # print(type(img_div), img_div)
    # print(img_div.a['href'])
    # print('- ' * 50)

    for ep_element in ep_list:
        if ep_element['ep_url'] == base_url + img_div.a['href']:
            for i in img_div.a:
                ep_element['ep_img_url'] = i['src']


# 第四步：访问ep_url跳转到新页面进行解析pdf_url和mp3_url。
for i in ep_list:
    if i['ep_url'] == "":
        pass
    else:
        sub_url = i['ep_url']
        sub_r = requests.get(sub_url)
        sub_html = sub_r.text.decode("utf-8")
        sub_soup = BeautifulSoup(sub_html, features="lxml")
        j = sub_soup.find_all("a", {"class": "download bbcle-download-extension-pdf"})
        for k in j:
            i['ep_pdf_url'] = k['href']

        j = sub_soup.find_all("a", {"class": "download bbcle-download-extension-mp3"})
        for k in j:
            i['ep_mp3_url'] = k['href']

        """
        {
            "ep_date": "Episode 190411 /   11 Apr 2019",
            "ep_title": u"The decluttering trend",
            "ep_url": "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-190411",
            "ep_pdf_url": "http://downloads.bbc.co.uk/learningenglish/features/6min/190411_6min_the_decluttering_trend.pdf",
            "ep_mp3_url": "http://downloads.bbc.co.uk/learningenglish/features/6min/190411_6min_the_decluttering_trend_download.mp3",
            "ep_brief": "Is it time you decluttered?",
            "ep_img_url": "http://ichef.bbci.co.uk/images/ic/976xn/p07271s6.jpg"
        }
        """


        # 第五步：已经准备好所有数据，开始下载。
        base_dir = "/var/www/html/bbc_6_minute_english/"
        download_dir = base_dir + i['ep_date'].replace('/', '-')

        if not os.path.exists("%s" % download_dir):
            os.makedirs("%s" % download_dir)

        for download_url in i['ep_img_url'], i['ep_pdf_url'], i['ep_mp3_url']:
            tmp_list = download_url.split("/")
            download_file = download_dir + "/" + tmp_list[-1]
            cmd = "wget \"%s\" -O \"%s\"" % (download_url, download_file)
            print(cmd)
            subprocess.call(cmd, shell=True)



