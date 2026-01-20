# find 2nd lowest numeber from list.

list=[10,12,0,2,3,3,4,4,5,6,6,9,1]

# for first lowest number :

min=list[0]
for i in list:
	if(i<min):
		min=i
# for second lowest number

min2=list[0]
for i in list:
	if(i<min2 and i>min):
		min2=i

print("the 2nd loewst number is :",min2)

# second way :

# first convet list in ascending order then print list[2].


