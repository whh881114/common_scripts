# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

# numpy提供了标准的三角函数：sin(), cos()和tan()。
a = np.array([0, 30, 45, 60, 90])
print('不同角度的正弦值：', end='')
# 通过乘pi/180转化为弧度
print(np.sin(a*np.pi/180), end='\n\n')
print('数组中角度的余弦值：', end='')
print(np.cos(a*np.pi/180), end='\n\n')
print('数组中角度的正切值：', end='')
print(np.tan(a*np.pi/180), end='\n\n')


#  arcsin()，arccos()和arctan()函数返回给定角度的sin，cos和tan的反三角函数。
a = np.array([0, 30, 45, 60, 90])
print('含有正弦值的数组：', end='')
sin = np.sin(a*np.pi/180)
print(sin)
print('计算角度的反正弦，返回值以弧度为单位：', end='')
inv = np.arcsin(sin)
print(inv)
print('通过转化为角度制来检查结果：', end='')
print(np.degrees(inv), end='\n\n')
print('- ' * 50)


print('arccos和arctan函数行为类似：', end='')
cos = np.cos(a*np.pi/180)
print(cos, end='\n\n')
print('反余弦：', end='')
inv = np.arccos(cos)
print(inv, end='\n\n')
print('角度制单位：', end='')
print(np.degrees(inv), end='\n\n')

print('tan函数：', end='')
tan = np.tan(a*np.pi/180)
print(tan, end='\n\n')

print('反正切：', end='')
inv = np.arctan(tan)
print(inv, end='\n\n')
print('角度制单位：', end='')
print(np.degrees(inv))