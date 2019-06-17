# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

"""
bitwise_and()   函数对数组中整数的二进制形式执行位与运算。

bitwise_or()    函数对数组中整数的二进制形式执行位与运算。

invert()        函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0。
                对于有符号整数，取该二进制数的补码，然后 +1。二进制数，最高位为0表示正数，最高位为 1 表示负数。
                -----------------------------------------------------------------------------------
                看看 ~1 的计算步骤：
                1. 将1(这里叫：原码)转二进制 ＝ 00000001
                2. 按位取反 ＝ 11111110
                3. 发现符号位(即最高位)为1(表示负数)，将除符号位之外的其他数字取反 ＝ 10000001
                4. 末位加1取其补码 ＝ 10000010
                5. 转换回十进制 ＝ -2
                -----------------------------------------------------------------------------------
                
left_shift()    函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的0。
"""
a, b = 13, 17
print('%d和%d的二进制形式：' % (a, b))
print(bin(a), bin(b))
print('')

print('%d和%d的位与：' % (a, b))
print(np.bitwise_and(a, b), bin(np.bitwise_and(a, b)))
print('')

print('%d和%d的位或：' % (a, b))
print(np.bitwise_or(a, b), bin(np.bitwise_or(a, b)))
print('')

x, y = 13, 242
print('%d的位反转，其中ndarray的dtype是unit8：' % x, end='')
print(np.invert(np.array([x], dtype=np.uint8)))
print('')

print('%d的二进制表示：' % x, end='')
print(np.binary_repr(x, width=8))
print('')

print('%d的二进制表示：' % y, end='')
print(np.binary_repr(y, width=8))
print('')

num = 10
print('%d的二进制表示：' % num, end='')
print(np.binary_repr(num, width=8))
print('将%d左移两位：' % num, end='')
print(np.left_shift(10, 2))
print('')

num = 40
print('%d的二进制表示：' % num, end='')
print(np.binary_repr(40, width=8))
print('将%d右移两位：' % num, end='')
print(np.right_shift(40, 2))
print('')
