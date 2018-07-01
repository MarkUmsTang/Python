#n = 2为默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(power(5))
print(power(5, 2))
print(power(5, 3))
#从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数


def enroll(name, gender, age=6, city='Beijing'):
    print('name:',name)
    print('gender:', gender)
    print('age', age)
    print('city', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjing')


# 定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=[]):
    L.append('End')
    return L

def my_add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print(add_end())
print(add_end())
print(add_end())


print(my_add_end())
print(my_add_end())
print(my_add_end([1,2]))
print(my_add_end([1,2]))



#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1, 2))
print(calc())

nums = [1,2,3]
print(calc(*nums))


def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)



#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def my_person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
#def person(name, age, *args, city, job):
#    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#person('Jack', 24, 'Beijing', 'Engineer')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: person() takes 2 positional arguments but 4 were given


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)

print(f1(1,2))
print(f1(1,2, c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99, ext=None))

#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
args = (1,2,3,4)
kw = {'d':99, 'x':'#'}
print(f1(*args, **kw))
args = (1,2,3)
kw = {'d':88, 'x':'#'}
print(f2(*args, **kw))












