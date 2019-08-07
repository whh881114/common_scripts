# -*- coding: UTF-8 -*-

"""
函数功能：
['default', 'master', 'redis'] ---> {"defalut":{"master":{"redis":{}}}}
"""

def list_2_dict(list):
    ret = {}
    dict_tail = {}
    dict_tail[list[0]] = ''

    for i in list[1:]:
        head = {}
        head[i] = dict_tail
        dict_tail = head
        ret = head
    print('- ' * 50)
    list.reverse()
    print("Origin list: %s" % list)
    print("Coverted dict: %s" % ret)


def main():
    lists = [
        ['default', 'master', 'redis'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    ]

    for list in lists:
        list.reverse()
        list_2_dict(list)


if __name__ == "__main__":
    main()