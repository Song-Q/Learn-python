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
        

#设置默认参数（必选参数在前，默认参数在后），默认参数必须指向不变对象
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city', city)
    

#可变参数（在参数前面加了一个*号）
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

calc(1, 2)
#5
nums = [1, 2, 3]
calc(*nums)

#关键字参数(允许传入任意个含参数名的参数，都会在函数内被组装为一个dict)
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数(命名关键字参数需要一个特殊分隔符*，*后面
#的参数被视为命名关键字参数)
def person(name, age, *, city, job):
    print(name, age, city, job)
#命名关键字参数必须传入参数名
person('Jack', 24, city='Beijing', job='Engineer')

#*args是可变参数，args 接收的是一个tuple
#**kw是关键字参数，kw 接收的是一个dict
