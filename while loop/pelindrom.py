# find number is pelindrom or not
# ex : 121 reverse = 121 so number is pelindrom.

n=int(input("enter the value of n :"))
sum=0
orignal_num=n

while(n>0):
	rem=n%10
	sum=sum*10+rem
	n=int(n/10)

print("reverse num  is :",sum)

if(sum==orignal_num):
	print("num is pelindrome")
	
else:
	print("num is  not pelindrome") 