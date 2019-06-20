# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

# numpy.amin()用于计算数组中元素沿指定轴的最小值。
# numpy.amax()用于计算数组中元素沿指定轴的最大值。

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('我们的数组是：')
print(a, end='\n\n')

print('调用amin()函数：')
print(np.amin(a, 1), end='\n\n')
print('再次调用amin()函数：')
print(np.amin(a, 0), end='\n\n')

print('调用amax()函数：')
print(np.amax(a), end='\n\n')
print('再次调用amax()函数：')
print(np.amax(a, axis=0), end='\n\n')

print('调用ptp()函数：')
print(np.ptp(a), end='\n\n')
print('沿轴1调用ptp()函数：')
print(np.ptp(a, axis=1), end='\n\n')
print('沿轴0调用ptp()函数：')
print(np.ptp(a, axis=0), end='\n\n')