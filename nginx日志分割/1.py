# -*- coding: UTF-8 -*-
from __future__ import print_function

a = [1, 2, 4, 5, 7, 9, 11, 14]
b = [1, 2, 4, 5, 7, 9, 11, 14]

# [1, 2, 4] [5, 7] [9, 11], [14]



# for index,value in enumerate(a):
#     print(index, value)

print(a)

base_num = a[0]
new_nums = []
# new_nums.append(base_num)
# for e in a[1:]:
for e in a:
    # print("e = ", e)
    if base_num + 3 >= e:
        new_nums.append(e)
    else:
        print(new_nums)
        # 重新初始化
        new_nums = []
        new_nums.append(e)
        base_num = e
        # print("base_num = %d" % e)
        # print("a = ", a)




# for a_elem in a:
#     index = 0
#     first_elem = a_elem
#     print('first a: ', a)
#     print('first_elem_a: ', first_elem)
#     for b_elem in b:
#         print('first b: ', b)
#         if first_elem + 3 >= b_elem:
#             index += 1
#             print(b_elem, end=' ')
#         else:
#             a = b[index:]
#             b = b[index:]
#             print('second a:', a)
#             print('second b:', b)
#             print(end='\n')
#             print('- ' * 50)