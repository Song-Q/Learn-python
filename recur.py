#为解决递归调用使用尾递归优化
#然后python并没有对尾递归做优化，实际过深的递归还是存在栈溢出
#计算n!
def fact(n):
    return fact_iter(n, 1)
    
def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num-1, num*product)
    

#practice 汉诺塔
#将递归问题拆解为二阶递归，考虑最后一步干什么，重复的步骤，和最后之前一步干什么
def hanoi(n, a, b, c)
    if n == 1:
        print(a, '-->', c)
    hanoi(n-1, a, c, b)
    print(a, '-->', c)
    hanoi(n-1, b, a, c)
    