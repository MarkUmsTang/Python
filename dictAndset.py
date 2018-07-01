#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#增加元素
d['Adam'] = 67

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
d['Jack'] = 88
#这时 d['Jack'] = 88

#如果key不存在，dict就会报错，要避免key不存在的错误，有两种办法，一是通过in判断key是否存在： 'Thomas' in d        二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：d.get('Thomas')返回None    d.get('Thomas', -1)返回-1  



#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
#dict内部存放的顺序和key放入的顺序是没有关系的    

