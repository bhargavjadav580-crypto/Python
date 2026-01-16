#using import method

def even_odd(n):
	if n%2==0:
		print('Even Number')
	else:
		print('Odd Number')

def addn(n):
	sum=0
	for i in range(1,n+1):
		sum = sum + i
	print('Sum =',sum)

def muln(n):
	mul=1
	for i in range(1,n+1):
		mul = mul * i
	print('Mul =',mul) 