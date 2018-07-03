#迭代

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i, secondvlaue in enumerate(['A', 'B', 'C']):
    print(i, secondvlaue)


#练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if (0 == len(L)):
        return (None, None)
    else:
        maxnumber = L[0]
        minnumber = L[0]
        for n in L:
            if n > maxnumber:
                maxnumber = n
            if n < minnumber:
                minnumber = n
        return (minnumber, maxnumber)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

