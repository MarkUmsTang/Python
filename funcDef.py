#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
my_abs('123')


def quadratic(a, b, c):
   s = b*b - 4*a*c
   if a == 0:
       x = -c / b
       return x
   elif s==0:
         x = -b / 2*a
         return x
   elif s < 0:
       return 'no anwser'
   else:
         x = (-b + math.sqrt(s)) / (2 * a)
         y = (-b - math.sqrt(s)) / (2 * a)
         return x, y

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

