# -*- coding: UTF-8 -*-


# 网页中有中文，需要重装载入sys并设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import requests

# 这里的代码是伪代码，只是示例。

# 示例：下载图片（小文件）。
r = requests.get(IMAGE_URL)
with open("./img/image2.png", "wb") as f:
    f.write(r.content)


# 示例：下载视频，镜像（大文件）。
r = requests.get(VIDEO_URL, stream=True)
with open("./img/image3.png", "wb") as f:
    for chuck in r.iter_content(chunk_size=32):
        f.write(chuck)

