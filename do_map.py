#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# -*- coding: utf-8 -*-
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#practice 将一个单词首字母大写，其余小写
def normalize(name):
    if isinstance(name, str) == True:
        return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


