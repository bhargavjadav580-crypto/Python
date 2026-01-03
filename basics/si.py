# find simple interest

amount = int(input('Enter the Amount :'))
rate   = int(input('Enter the Rate of Interest :'))
year   = int(input('Enter the Years :'))

ans = (amount * rate * year) / 100
print('Simple Interest =',ans)