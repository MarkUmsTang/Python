names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)


#range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
	sum = sum + x
print(sum)



sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)


#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
i = 0
while i < len(L):
	print(L[i])
	i = i + 1

# break continue都适用