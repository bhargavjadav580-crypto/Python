from area import arearectangle,areasquare,areacircle

print("which shapes area you want ")
print("choose 1 for rectangle area ")
print("choose 2 for square area ")
print("choose 3 for circle area ")

choice=int(input("enter your choice : "))

if(choice==1):
	length=int(input("enter the value of length : "))
	breadh=int(input("enter the value of breadh : "))
	arearectangle(length,breadh)

elif(choice==2):
	length=int(input("enter the value of length : "))
	areasquare(length) 

elif(choice==3):
	radius=int(input("enter the radius :"))
	areacircle(radius)
else:
	print("please enter number between 1 to 3")
