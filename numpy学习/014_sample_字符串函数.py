# -*- coding: UTF-8 -*-

from __future__ import print_function
import numpy as np

print('连接两个字符串：', end='')
print(np.char.add(['hello'], [' xyz']), end='\n\n')

print('连接示例：', end='')
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']), end='\n\n')

print('字符串多重连接：', end='')
print(np.char.multiply('Runoob ', 3), end='\n\n')

print('将字符串居中：', end='')
print(np.char.center('Runoob', 20, fillchar='*'), end='\n\n')

print('将第一个字母转换为大写：', end='')
print(np.char.capitalize('runoob'), end='\n\n')

print('将每个单词的第一个字母转换为大写：', end='')
print(np.char.title('i like runoob'), end='\n\n')

print('将每个字母转换为小写：', end='')
print(np.char.lower(['RUNOOB', 'GOOGLE', 'MIRCOSOFT']), end=' ')
print(np.char.lower('RUNOOB'), end='\n\n')


print('将每个字母转换为大写：', end='')
print(np.char.upper(['runoob', 'google', 'mircosfot']), end=' ')
print(np.char.upper('runoob'), end='\n\n')

print('将句子分隔：', end='')
print(np.char.split('i like runoob?'), end=' ')
print(np.char.split('www.runoob.com', sep='.'), end='\n\n')

# \n，\r，\r\n 都可用作换行符。
print('按换行符作为分隔符来分割字符串：', end='')
print(np.char.splitlines('i\nlike runoob?'), end=' ')
print(np.char.splitlines('i\rlike runoob?'), end='\n\n')

print('numpy.char.strip() 函数用于移除开头或结尾处的特定字符。')
print(np.char.strip('ashok arunooba', 'a'))
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

print('numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串。')
print(np.char.join(':', 'runoob'))
print(np.char.join([':', '-'], ['runoob', 'google']), end='\n\n')

print('numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。')
print(np.char.replace('I like runoob.', 'oo', 'cc'))

print('numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。')
a = np.char.encode('runoob', 'cp500')
print(a)

print('numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。')
print(np.char.decode(a, 'cp500'))