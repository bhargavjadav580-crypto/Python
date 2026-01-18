from mul_sum_sub import sum,mul,sub,div

x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))

print("what do you want :")
print("choose 1 for sum")
print("choose 2 for mul")
print("choose 3 for sub")
print("choose 4 for div")

choise=int(input("enter your choise : "))

if(choise==1):
	sum(x,y)
elif(choise==2):
	mul(x,y)
elif(choise==3):
	sub(x,y)
elif(choise==4):
	div(x,y)
else:
	print("please enter the valid number")  

