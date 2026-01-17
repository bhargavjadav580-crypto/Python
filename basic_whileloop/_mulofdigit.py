# find multiplication of digit

n=int(input("enter the digit :"))
mul=1
while(n>0):
	rem=n%10
	mul=mul*rem
	n=int(n/10)
   
print("mul is :",mul)    