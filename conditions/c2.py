# markhseet
maths  = int(input('Enter Marks of Maths :'))
sci    = int(input('Enter Marks of Science :'))
java   = int(input('Enter Marks of Java :'))
php    = int(input('Enter Marks of PHP :'))
python = int(input('Enter Marks of Python :'))

total_marks = maths + sci + java + php + python
print("Total Marks =",total_marks)

per = total_marks / 5
print('Percentage =',per)

if per<30:
	print("Sorry you are failed...")
elif (per>=30) and (per<50):
	print("Second class")
elif (per>=50) and (per<80):
	print("FIrst class")
else:
	print("Distiction")

