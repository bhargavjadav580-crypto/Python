# Check if year is a leap year

year = int(input("enter your year  : "))

if year%400==0 and year%100==0:
	print("given year is leap year")

elif year%4==0 and year%100!=0:
	print("given year  leap year")
else:
	print("given year is not leap year")