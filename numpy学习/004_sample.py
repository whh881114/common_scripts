# -*- coding: UTF-8 -*-

import numpy as np

a = np.arange(24)
print(a, a.ndim)
print('\n')


b = a.reshape(2, 4, 3)
print(b, b.ndim)
print('\n')


a = np.array([[1, 2, 3], [4, 5, 6]])
print(a, a.shape)
print('\n')


a = np.array([[1, 2, 3], [ 4, 5, 6]])
print(a)
a.shape = (3, 2)
print(a)
print('\n')


a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)
print('\n')


# ndarray.itemsize以字节的形式返回数组中每一个元素的大小。
# 数组的dtype为int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
print('\n')

# 数组的dtype现在为float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)
print('\n')


x = np.array([1, 2, 3, 4, 5])
print(x.flags)
print('\n')
"""
C_CONTIGUOUS (C) 	数据是在一个单一的C风格的连续段中
F_CONTIGUOUS (F) 	数据是在一个单一的Fortran风格的连续段中
OWNDATA (O) 	    数组拥有它所使用的内存或从另一个对象中借用它
WRITEABLE (W) 	    数据区域可以被写入，将该值设置为 False，则数据为只读
ALIGNED (A) 	    数据和所有元素都适当地对齐到硬件上
UPDATEIFCOPY (U) 	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
"""