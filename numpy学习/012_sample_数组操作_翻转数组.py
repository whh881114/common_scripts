# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

"""
numpy.transpose

numpy.transpose 函数用于对换数组的维度，格式如下：

numpy.transpose(arr, axes)

参数说明:

    arr：要操作的数组
    axes：整数列表，对应维度，通常所有维度都会对换。
"""
a = np.arange(12).reshape(3, 4)
print('原数组：')
print(a)
print('\n')
print('对换数组（将原数组的维度对换，如原数组是3*4维度，现换成4*3）。')
print(np.transpose(a))

"""
numpy.ndarray.T 类似 numpy.transpose：
"""
print('使用numpy.ndarray.T完成transpose功能。')
print(a.T)
print('\n')


"""
numpy.rollaxis

numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：

numpy.rollaxis(arr, axis, start)

参数说明：

    arr：数组
    axis：要向后滚动的轴，其它轴的相对位置不会改变
    start：默认为零，表示完整的滚动。会滚动到特定位置。
"""
# 创建三维的ndarray
a = np.arange(8).reshape(2, 2, 2)
print('原数组：')
print(a)
print('\n')

print('将轴2滚动到轴0（宽度到深度），调用rollaxis函数：')
print(np.rollaxis(a, 2))
print('\n')
print('将轴0滚动到轴1（宽度到高度），调用rollaxis函数：')
print(np.rollaxis(a, 2, 1))


"""
numpy.swapaxes

numpy.swapaxes 函数用于交换数组的两个轴，格式如下：

numpy.swapaxes(arr, axis1, axis2)

    arr：输入的数组
    axis1：对应第一个轴的整数
    axis2：对应第二个轴的整数

"""
a = np.arange(8).reshape(2, 2, 2)
print('原数组：')
print(a)
print('\n')
print('现在交换轴0（深度方向）到轴2（宽度方向），调用swapaxes函数后数组：')
print(np.swapaxes(a, 2, 0))