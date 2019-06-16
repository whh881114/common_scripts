# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

# 修改数组形状
"""
numpy.reshape
numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')

    arr：要修改形状的数组
    newshape：整数或者整数数组，新的形状应当兼容原有形状
    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。

"""
a = np.arange(8)
print('原始数组：')
print(a)
b = a.reshape(4, 2)
print('修改后的数组：')
print(b)
print('- ' * 50)


"""
numpy.ndarray.flat, 它是一个数组元素迭代器。
"""
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器。
print('迭代后的数组：')
for element in a.flat:
    print(element, end=',')
print('\n')
print('- ' * 50)


"""
numpy.ndarray.flatten

numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：

ndarray.flatten(order='C')

参数说明：

    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
"""
a = np.arange(8).reshape(2, 4)
print('原始数组：')
print(a)
print('\n')

print('展开的数组（默认按行遍历）')
print(a.flatten())

print('以F风格（按列遍历）展开数组')
print(a.flatten(order='F'))
print('- ' * 50)

"""
numpy.ravel

numpy.ravel()展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），
修改会影响原始数组。

该函数接收两个参数：

numpy.ravel(a, order='C')

参数说明：

    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
"""
a = np.arange(8).reshape(2, 4)
print('原始数组：')
print(a)
print('\n')
print('调用ravel函数之后：')
print(a.ravel())
print('\n')

print('以F风格顺序调用ravel函数之后：')
print(a.ravel(order='F'))