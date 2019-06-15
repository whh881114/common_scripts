# -*- coding: UTF-8 -*-

import numpy as np

# empty用于未初始化的数组。
x = np.empty([3, 2], dtype=int)
print(x)
print('\n')

# zeros用0来填充数组。
# 默认为浮点数
x = np.zeros(5)
print(x)
print('\n')

# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)
print('\n')

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)
print('\n')


# ones用1来填充。
# 默认为浮点数
x = np.ones(5)
print(x)
print('\n')

# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)
print('\n')