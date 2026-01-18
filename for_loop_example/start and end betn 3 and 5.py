# find sum,multipication,division if number div by 3and5.


# for sum

start=int(input("enter the number :"))
end=int(input("enter the number :"))
sum=0
for i in range(start,end+1):
	if(i%3==0 and i%5==0):
		sum=sum+i
print("sum is :",sum)

# for mul

start=int(input("enter the number :"))
end=int(input("enter the number :"))
mul=1
for i in range(start,end+1):
	if(i%3==0 and i%5==0):
		mul=mul*i
print("mul is :",mul)

# for count

start=int(input("enter the number :"))
end=int(input("enter the number :"))
count=0
for i in range(start,end+1):
	if(i%3==0 and i%5==0):
		count=count+1
print("count is :",count)
print("sum : mul : count : ",sum,mul,count)



