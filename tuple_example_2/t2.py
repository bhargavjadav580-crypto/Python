# input tuple  and remove duplicate valur from tuple
n = int(input("enter how many number you want to insert : "))
tup1 = ()

for i in range(n):
	number = int(input("enter the number : "))
	tup1=tup1+(number,)

ori_tup = ()
for i in tup1:
	if i not in ori_tup:
		ori_tup = ori_tup + (i,)

print("new tuple is : ",ori_tup)
 