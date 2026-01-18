# find number upto 2 qube and sum

n=int(input("emter the number : "))
sum=0
for i in range(n,1,-1):
	cube=i*i*i
	sum=sum+cube
print("the cube is :",sum)
