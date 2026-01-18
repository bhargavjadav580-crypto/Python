def armstrong(n):
	sum=0
	temp=n
	while(n>0):
		rem=n%10
		sum=sum+rem*rem*rem
		n=int(n/10)
	print("sum is :",sum)
	if(temp==sum):
		print("armstrong number")
	else:
		print("not an armstrong number")

#pelindrom number 

def pelindrom(n):
	sum=0
	temp=n 
	while(n>0):
		rem=n%10
		sum=sum*10+rem
		n=int(n/10)
	print("sum is :",sum)
	if(temp==sum):
		print("pelindrom number")
	else:
		print("not pelindrom number")

#reverse numnber 

def reverse(n):
	sum=0
	while(n>0):
		rem=n%10
		sum=sum*10+rem
		n=int(n/10)
	print("sum is :",sum)
	
