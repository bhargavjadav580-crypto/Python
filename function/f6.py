#mul of number in series
def muln(n):
	mul = 1
	for i in range(1,n+1):
		mul = mul * i
	print('Mul =',mul)


num = int(input('Enter a Number :'))
muln(num) 