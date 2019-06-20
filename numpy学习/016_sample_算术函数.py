# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

print('第一个数组：')
a = np.arange(9, dtype=np.float_).reshape(3, 3)
print(a, end='\n\n')

print('第二个数组：')
b = np.array([10, 10, 10])
print(b, end='\n\n')

print('这两个数组相加：')
print(np.add(a, b), end='\n\n')

print('这两个数组相减：')
print(np.subtract(a, b), end='\n\n')

print('这两个数组相乘：')
print(np.multiply(a, b), end='\n\n')

print('这两个数组相除：')
print(np.divide(a, b), end='\n\n')

# numpy.reciprocal()返回参数逐元素的倒数。
a = np.array([0.25, 1.33, 1, 100])
print('我们的数组是：')
print(a, end='\n\n')
print('调用reciprocal函数后，数组内容为：')
print(np.reciprocal(a))


# numpy.power()函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中的相应元素的幂。
a = np.array([10, 100, 1000])
print('我们的数组是：')
print(a, end='\n\n')

print('数组调用power函数后：')
print(np.power(a, 2))

print('第二个数组：')
b = np.array([1, 2, 3])
print(b, end='\n\n')

print('再次谳用power函数后：')
print(np.power(a, b))

# numpy.mod()计算输入数组中相应元素的相除后的余数，函数numpy.remainder()也产生相同的结果。
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print('第一个数组：')
print(a, end='\n\n')
print('第二个数组：')
print(b, end='\n\n')
print('调用mod()函数：')
print(np.mod(a, b), end='\n\n')
print('调用remainder()函数：')
print(np.remainder(a, b), end='\n\n')