# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

"""
numpy.broadcast

numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。

该函数使用两个数组作为输入参数，如下实例：
"""
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print('x原始内容：')
print(x)
print('')
print('y原始内容：')
print(y)
print('')

print('对y广播x：')
b = np.broadcast(x, y)  # 它拥有iterator属性，基于自身组件的迭代器元组
r, c = b.iters
# python3为next(context)，python2为context.next()
print(r.next(), c.next())
print(r.next(), c.next())
print('\n')

print('对y广播x，其广播对象的形状：', end='')
print(b.shape)
print('')

# 手动使用broadcast将x与y相加
b = np.broadcast(x, y)
c = np.empty(b.shape)
print('手动使用broadcast将x与y相加：')
print(c.shape)
print('')
c.flat = [u + v for (u, v) in b]

print('调用flat函数：')
print(c)
print('\n')

# 获取了和numpy内建的广播支持相同的结果
print('x与y的和：')
print(x + y)


"""
numpy.broadcast_to

numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。 
如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。

numpy.broadcast_to(array, shape, subok)
"""
a = np.arange(4).reshape(1, 4)
print('原数组：')
print(a)
print('')

print('调用broadcast_to函数之后：')
print(np.broadcast_to(a, (4,4)))
print('')



"""
numpy.expand_dims

numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:

 numpy.expand_dims(arr, axis)

参数说明：

    arr：输入数组
    axis：新轴插入的位置
"""
x = np.array(([1, 2], [3, 4]))
print('数组x：')
print(x)
print('')

y = np.expand_dims(x, axis=0)
print('数组y：', end='')
print(y)
print('')

print('数组x和y的形状：', end='')
print(x.shape, y.shape)
print('')

print('在位置1插入轴之后的数组y:', end='')
y = np.expand_dims(x, axis=1)
print(y)
print('')

print('x.ndim和y.ndim：', end='')
print(x.ndim, y.ndim)
print('')

print('x.shape和y.shape：', end='')
print(x.shape, y.shape)


"""
numpy.squeeze

numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：

numpy.squeeze(arr, axis)

参数说明：

    arr：输入数组
    axis：整数或整数元组，用于选择形状中一维条目的子集

"""
x = np.arange(9).reshape(1, 3, 3)
print('数组x：')
print(x)
print('\n')

y = np.squeeze(x)
print('数组y：')
print(y)
print('\n')

print('数组x和数组y的形关：', end='')
print(x.shape, y.shape)