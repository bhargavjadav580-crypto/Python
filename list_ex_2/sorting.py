# sorting of list.


mylist = [2,5,7,4,1]
print(mylist)

for i in range(0,5):

	for j in range(i+1,5):
		
		if mylist[i] > mylist[j]:
			c = mylist[i]
			mylist[i] = mylist[j]
			mylist[j] = c

print(mylist)
# print('2nd Lowest =',mylist[1])
print('3rd highest =',mylist[2])