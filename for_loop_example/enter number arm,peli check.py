# enter a code for get armstrong,pelindrom,reverse number

n=int(input("enter the number: "))

code=int(input("enter the code :"))

if(code==1):
	sum=0
	orignal_num=n

	while(n>0):
		rem=n%10
		sum=sum+rem*rem*rem
		n=int(n/10)

	print("sum is :",sum)

	if(sum==n):
		print("armstrong number")
	else:
		print(" not armstrong number")
elif(code==2):
	sum=0
	orignal_num=n

	while(n>0):
		rem=n%10
		sum=sum*10+rem
		n=int(n/10)


	print("reverse num  is :",sum)

	if(sum==n):
		print("num is pelindrome")
	else:
		print("num is  not pelindrome") 
else:
	print("not dedined")


