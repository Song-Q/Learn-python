#list
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
#list的索引从0开始
#可以倒这获取索引 classmates[-1] >>> Tracy
classmates.append('Adam')    #向list中追加元素到末尾
classmates.insert(1, 'Jack')    #将元素插入到指定索引位置
#.pop()将会从末尾依次删除一个元素
classmates.pop(1)    #删除指定索引的元素
#list中的元素的数据类型可以不同，甚至可以包含另一个list，list可以为空


#tuple一旦初始化就不可修改（即元素的指向不可改变），没有append(),insert(),其它获取元素的方法与list相同classmates[-1]
classmates = ('Michael', 'Bob', 'Tracy')
#若定义的tuple中只有一个元素时，必须要在元素后加一个逗号来消除歧义t = ('Bob'，)；否则python会认为()是数学运算中的小括号
#tuple中元素可以为list，list本身可以改变


#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])