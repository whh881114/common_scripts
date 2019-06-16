# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

# python2在文件首行加上 from __future__ import print_function ，也可以使用python3中给end参数赋空(值)的方式实现输出不换行。

"""
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。

迭代器最基本的任务的可以完成对数组元素的访问。
"""

# 我们使用 arange() 函数创建一个 2X3 数组，并使用 nditer 对它进行迭代。
a = np.arange(6).reshape(2, 3)
print('原始数组是：')
print(a)
print('\n')

print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=',')
print('\n')
print('* ' * 50)


# 控制遍历顺序。
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a.T):
    print(x, end=',')
print('\n')
print('* ' * 50)

for x in np.nditer(a.T.copy(order='C')):
        print(x, end=',')
print('\n')
print('* ' * 50)
"""
从上述例子可以看出，a 和 a.T 的遍历顺序是一样的，也就是他们在内存中的存储顺序也是一样的，但是 a.T.copy(order = 'C') 的遍历结
果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。
控制遍历顺序

    for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
    for x in np.nditer(a.T, order='C'):C order，即是行序优先；

"""


a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('- ' * 50)

print('原始数组的转置是：')
b = a.T
print(b)
print('- ' * 50)

print('以C风格顺序排序：')
c = b.copy(order='C')
print(c)
print('- ' * 50)
for x in np.nditer(c):
    print(x, end=',')
print('\n')
print('* ' * 50)

print('以F风格顺序排序：')
c = b.copy(order='F')
print(c)
print('- ' * 50)
for x in np.nditer(c):
    print(x, end=',')
print('\n')
print('* ' * 50)


# 可以通过显示设置，来强制nditer对象使用某种顺序。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('以C风格顺序排序：')
for x in np.nditer(a, order='C'):
    print(x, end=',')
print('\n')
print('* ' * 50)
print('以F风格顺序排序：')
for x in np.nditer(a, order='F'):
    print(x, end=',')
print('\n')
print('* ' * 50)


# 修改数组中元素的值。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x
print('修改后的数组是：')
print(a)


# 使用外部循环。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')

for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=',')
print('\n')
print('* ' * 50)

# 广播迭代。
# 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，
# 则使用以下迭代器（数组 b 被广播到 a 的大小）。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('\n')

print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')

print('修改后的数组为：')
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=',')