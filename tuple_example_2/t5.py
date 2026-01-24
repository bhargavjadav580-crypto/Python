#print the square of tuple 


tuple1 = (1,2,3,4,5,6)

list1 = []
for i in tuple1:
	
	list1.append(i*i)
tuple2 = tuple(list1)

print(tuple2)
 