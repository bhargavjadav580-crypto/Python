# count positive,negative and zero

number=[1,2,0,8,7,0,8,6,-1,-2,-3]
count1=0
count2=0
count3=0
for i in number:
	if(i>0):
		count1=count1+1
	elif(i<0):
		count2=count2+1
	else:
		count3=count3+1
print("total positive number is :",count1)
print("total negative number is :",count2)
print("total zero is :",count3)

 
