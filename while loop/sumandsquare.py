#sum and square of digit

n=int(input("enter the digit :"))
sum=0
while(n>0):
	rem=n%10
	sum=sum+(rem*rem)
	n=int(n/10)
   
print("sum is :",sum)    