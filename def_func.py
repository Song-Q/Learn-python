def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-95))

#定义一个空函数
#def nop:
#    pass

#practice 返回一元二次方程的两个解
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        TypeError('bad operand type')
    delta = pow(b,2) - 4*a*c 
    if delta >= 0:
        x1 = (-b+math.sqrt(delta)) / (2*a)
        x2 = (-b-math.sqrt(delta)) / (2*a)
        return x1, x2
    else:
        print('The unary quadratic equation has no real number solution')