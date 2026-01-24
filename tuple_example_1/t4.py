# swaping in tuple

tup1 = (1,2,3,4,5)

list1 = list(tup1)
total = len(list1)

temp = list1[total-1]

list1[total-1] = list1[0]

list1[0] = temp

tup2 = tuple(list1)
print(tup2) 