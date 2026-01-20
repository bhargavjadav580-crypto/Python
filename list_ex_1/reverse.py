# print list in reverse.

list=[1,2,3,4,5,6]

for i in range(5,-1,-1):
	print(list[i])


# second way :
list=[1,2,3,4,5,6,3,8]
print(len(list))

for i in range(len(list),0,-1):
	print(i)

# third way 

print(list[::-1])
