# take input value and compare with list if same then count.

list = [1,2,3,45,2]
b = int(input("enter the value of b: "))
count=0
for i in list:
	if(i==b):
		count=count+1

if(count>0):
	print(count)
else:
	print("not match") 