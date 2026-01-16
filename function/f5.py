# addition of number in series

def addn(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + i
	print('Sum =',sum)


num = int(input('Enter a Number :'))
addn(num) 