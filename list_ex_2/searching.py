# find value exist in list or not.

mylist = [10, 20, 30, 40, 50]
num = 30

temp = 0

for i in mylist:   # loop through each element
    if i == num:
        print("Match Found")
        temp = temp + 1
        break   # exit loop once found

if temp == 0:
    print("Value Not Found")
