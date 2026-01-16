# using returns

def add(a,b):
	sum = a + b
	return sum

def mul(a,b):
	mul = a * b
	return mul

x = int(input('Enter a Number :'))
y = int(input('Enter a Number Again:'))

ans1 = add(x,y)
ans2 = mul(x,y)
ans = ans1 + ans2
print(ans)
 
