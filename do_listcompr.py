#列表生成式
#生成一个1-10的list
list(range(1,11))

#生成1-10的平方的list
[x*x for x in range(1,11)]
#筛选出仅偶数的平方
[x*x for x in range(1,11) if x%2 == 0]
#两层循环生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

#同时迭代dict的key和value
d = {'x':'A', 'y':'B', 'z':'C'}
for k,v in d.items():
    print(k, '=', v)
    
#等效于
d = {'x':'A', 'y':'B', 'z':'C'}
[k + '=' + v for k, v in d.items()]

#将list所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

#practice
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) == True]
print(L2)

