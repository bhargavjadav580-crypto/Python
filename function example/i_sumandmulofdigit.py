from sumandmulofdigit import sumdigit,mulofdigit

num=int(input("enter the value of num : "))

print("what do you want : ")
print("choose 1 for sum of digit : ")
print("choose 2 for mul of digit : ")

choise=int(input("enter your choise : "))

if(choise==1):
	sumdigit(num)

elif(choise==2):
	mulofdigit(num)
	
else:
	print("enter the valid number ")