# take start and end input and find number even or odd.

start=int(input("enter the number :"))
end=int(input("enter the number :"))
count1=0
count2=0

for i in range(start,end+1): 
	
	if(i%2==0):
		count1=count1+1
		print(count1,i,"even")
	else:
		count2=count2+1
		print(count2,i,"odd")
	
print("even number is :",count1)
print("odd number is : ",count2)
