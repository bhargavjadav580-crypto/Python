# sum of digit.

def sumdigit(n):
	sum=0

	while(n>0):
		rem=n%10
		sum=sum+rem
		n=int(n/10)

	print("sum is :",sum)

# mul of digit.

def mulofdigit(n):
	mul=1

	while(n>0):
		rem=n%10
		mul=mul*rem
		n=int(n/10)
		
	print("mul is :",mul)
