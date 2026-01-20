mylist = ['A','B','C','D','E','F']
print(mylist)

# add
mylist.append('G')
mylist.insert(2,'G')
mylist1 = ['G','H','I']
mylist.extend(mylist1)
print(mylist)

# get
print(mylist[4])
print(mylist[-2])

print(mylist[1:4])
print(mylist[3:5])
print(mylist[1:])
print(mylist[:4])
print(mylist[:])

print(mylist[-5:-2])
print(mylist[-4:-2])
print(mylist[-5:])
print(mylist[:-3])
print(mylist[:])

# delete
mylist.remove('D')
mylist.pop(1)
del mylist[1]
del mylist
mylist.clear()
print(mylist)

# update
mylist[3] = 'hello'
print(mylist)
  











