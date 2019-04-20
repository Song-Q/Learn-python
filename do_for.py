#生成一个从0开始的任意大整数序列的函数 range(5)
#for
sum = 0
for x in range(101):
    sum = sum + x 
print(sum)

#while 
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#practice
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s' %name)

#当程序进入死循环是可以使用Ctrl+C退出程序
