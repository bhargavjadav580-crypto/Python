from while_functions import armstrong,pelindrom,reverse

num = int(input('Enter a Number :')) 

print('What would you like to do with This Number ?')
print('Enter 1 For Armstrong Number')
print('Enter 2 For Palindrome Number')
print('Enter 3 For Reverse Number')

choice = int(input('Enter Your Choice'))

if choice == 1:
	armstrong(num)

elif(choice==2):
	pelindrom(num)
elif choice==3:
	Reverse(num)
else:
	print('Invalid Choice.....Please Try Bteween 1 to 3') 