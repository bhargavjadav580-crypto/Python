n=int(input("emter the number : "))
sum=0
while(n>0):
	rem=n%10
	sum=sum+rem*rem*rem
	n=int(n/10)

print("sum is :",sum)

if(sum%2==0):
	print("sum is even")
else:
	print("the sum is odd")


# using for loop 

n = int(input("enter the n  ; "))

for i in range(1,n+1):
	if i==n:
		qube  = i*i*i
print("qube of ",n, 'is :',qube)

