# swap using third variable

a = int(input('Enter a Number :'))
b = int(input('Enter a Number Again:'))

print('Before Swapping A =',a)
print('Before Swapping B =',b)

# swapping logic
c = a
a = b
b = c

print('After Swapping A =',a)
print('After Swapping B =',b)