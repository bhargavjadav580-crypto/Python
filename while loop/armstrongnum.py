# find number is armstrong or not

n = int(input("enter the value of n :"))
sum=0
orignal_num = n 

while(n>0):
	rem=n%10
	sum=sum+rem*rem*rem
	n=int(n/10)

print("sum is :",sum)

if(sum==orignal_num):
	print("armstrong number")
else:
	print(" not armstrong number")

