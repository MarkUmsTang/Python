#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

x = 1
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
 	print('True')



#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：

high = 1.75
weight = 80.5
bmi = weight/(high*high)

#一定不要忘了冒号
if bmi < 18.5:
    print('00前')
elif bmi < 25:
	print('体重正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')



s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')