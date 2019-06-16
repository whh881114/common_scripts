# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

"""
numpy.concatenate

numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：

numpy.concatenate((a1, a2, ...), axis)

参数说明：

    a1, a2, ...：相同类型的数组
    axis：沿着它连接数组的轴，默认为 0

"""
print('第一个数组：')
a = np.array([[1, 2], [3, 4]])
print(a)
print('')

print('第二个数组：')
b = np.array([[5, 6], [7, 8]])
print(b)
print('')

print('沿轴0连接两个数组：')
print(np.concatenate((a, b)))
print()

print('沿轴1连接两个数组：')
print(np.concatenate((a, b), axis=1))
print('- ' * 50)


"""
numpy.stack

numpy.stack 函数用于沿新轴连接数组序列，格式如下：

numpy.stack(arrays, axis)

参数说明：

    arrays相同形状的数组序列
    axis：返回数组中的轴，输入数组沿着它来堆叠

"""
print('沿轴0堆叠两个数组：')
print(np.stack((a, b), 0))

print('沿轴1堆叠两个数组：')
print(np.stack((a, b), 1))
print('- ' * 50)


"""
numpy.hstack

numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
"""
print('水平堆叠：')
c = np.hstack((a, b))
print(c)
print('- ' * 50)


"""
numpy.vstack
numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。 
"""
print('竖直堆叠：')
c = np.vstack((a, b))
print(c)
print('- ' * 50)
