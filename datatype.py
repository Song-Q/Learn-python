#r'内容' 表示内部字符串默认不转义
#允许用'''...'''来表示多行内容
print(123)
print(456.789)
print('Hello, world')
print('Hello, \'Adam\'')
print(r'Hello, "Bart"')
print(r'''Hello,
Lisa!''')

#ord()函数获取字符的编码
#chr()函数把编码转换为字符

#将字符串从Unicode转变为UTF-8;从UTF-8转变为Unicode
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#占位符：%d 整数  %f 浮点数  %s 字符串  %x 十六进制整数
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明的成绩从去年的%d分提升到了今年的%d分，他成绩提升的百分点为%.2f%%' % (s1, s2, r))

