# -*- coding: UTF-8 -*-
from __future__ import print_function

import time

nginx_access_log = 'nginx_access.log'
nginx_access_log = 'access.log201907121562868878'

with open(nginx_access_log, 'r') as f:
    logs = f.readlines()
f.close()

time_stamps = []
for log_entry1 in logs:
    # print('- ' * 50)
    # print(log_entry1)
    # print('- ' * 50)
    try:
        line1 = log_entry1.split(' ')
        time_tag1 = line1[3].replace('[', '').replace(']', '').split(',')[0]
        time_array1 = time.strptime(time_tag1, "%d/%b/%Y:%H:%M:%S")
        time_stamp1 = int(time.mktime(time_array1))
        time_stamps.append(time_stamp1)
    except:
        pass
        # 消除日志格式不一样的记录，如第一段有三个IP地址。

# 去重并排序
time_stamps = list(set(time_stamps))
time_stamps.sort()

# print("总时间戳列表：", time_stamps, end='\n\n')

base_time_stamp = time_stamps[0]
new_time_stamps = []
for time_stamp2 in time_stamps:
    if base_time_stamp + 60 >= time_stamp2:
        new_time_stamps.append(time_stamp2)
    else:
        # 此时经过for循环后，已经分段了，接下来就是要对每个段做处理了。
        # print(new_time_stamps)

        first_time_stamp = new_time_stamps[0]
        last_time_stamp = new_time_stamps[-1]
        first_time_array = time.localtime(first_time_stamp)
        last_time_array = time.localtime(last_time_stamp)
        print("时间段：%s -- %s" % (time.strftime("%Y/%m/%d %H:%M:%S", first_time_array), time.strftime("%Y/%m/%d %H:%M:%S", last_time_array)))

        http_codes = []
        for log_entry3 in logs:
            try:
                line3 = log_entry3.split(' ')
                time_tag3 = line3[3].replace('[', '').replace(']', '').split(',')[0]
                time_array3 = time.strptime(time_tag3, "%d/%b/%Y:%H:%M:%S")
                time_stamp3 = int(time.mktime(time_array3))
                if time_stamp3 in new_time_stamps:
                    http_codes.append(line3[8])
            except:
                pass

        set_http_codes = list(set(http_codes))
        for code in set_http_codes:
            print("http_code：%3s  summary_count: %d  average_count: %.2f\n" % (code, http_codes.count(code), http_codes.count(code)/60.0))


        # 这个是做下一个段的初始工作。
        new_time_stamps = []
        new_time_stamps.append(time_stamp2)
        base_time_stamp = time_stamp2

        # print(new_time_stamps)
        # print(base_time_stamp)

