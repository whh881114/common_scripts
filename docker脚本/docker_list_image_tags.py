# -*- coding: UTF-8 -*-

"""
Author: Roy Wong (whh881114@gmail.com)
Date: 2019/08/26
Description: List the tags which you search a docker image.
"""
from __future__ import print_function

import json
import argparse
import requests
from natsort import natsorted

DOCKERHUB_URL = "https://registry.hub.docker.com/v1/repositories"
TIMEOUT = 10


def usage():
    global image

    parser = argparse.ArgumentParser(description="List the tags which you search a docker image.")
    parser.add_argument('--image', '-i', required=True, type=str)
    args = parser.parse_args()
    image = args.image


def list_image_tags(image):
    image_url = "{}/{}/tags".format(DOCKERHUB_URL, image)
    try:
        r = requests.get(image_url, timeout=TIMEOUT)
    except requests.exceptions.ConnectTimeout as e:
        print(e)

    tags = [ i['name'] for i in json.loads(r.text)]
    # tags.sort(key=lambda d:int(d))
    print('The tags of the image "%s" are under the line.' % image)
    print('* ' * 60)
    tags = natsorted(tags)
    for i in tags:
        print("%-25s" % i, end='')
        if tags.index(i) != 0 and (tags.index(i) + 1) % 5 == 0:
            print('')
    print('\n')


def main():
    usage()
    list_image_tags(image)


if __name__ == '__main__':
    main()
