# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

# numpy.around(a, decimals)，返回指定数字的四舍五入值。
# a: 数组
# decimals: 舍入的小数位数。默认值为0。如果为负，整数将四舍五入到小数点左侧的位置。

a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print('原数组：', end='')
print(a)

print('舍入后：')
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=2))
print(np.around(a, decimals=-1))
print('- ' * 50)

# numpy.floor()返回数字的下舍整数。
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print('提供的数组：', end='')
print(a)
print('修改后的数组：', end='')
print(np.floor(a))

# numpy.ceil()返回数字的上入整数。
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print('提供的数组：', end='')
print(a)
print('修改后的数组：', end='')
print(np.ceil(a))