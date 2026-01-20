# write a program for sum,mul,count in list.


mylist = [1,2,4,5,7,8,10,12,14,20,25,30]
sum = 0
mul = 1
count = 0

for i in mylist:
	if i % 5 == 0:
		sum = sum + i
		mul = mul * i
		count = count + 1

print('Sum =',sum)
print('Multiplication =',mul)
print('Count =',count) 