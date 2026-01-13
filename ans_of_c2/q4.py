# 4. Car Rental Billing
# Rental charges:
# - ₹500 per day for first 5 days
# - ₹400 per day for next 5 days
# - ₹300 per day for remaining days
# Input number of days and calculate total rent.

day=float(input("enter the day :"))

if (day>=1 and day<=5):
	rent=day*500
	print("the rent is :",rent)

elif(day>=6 and day<=10):
	newday=day-5
	rent=(newday*400)+2500
	print("the rent is :",rent)
else:
	newday=day-10
	rent=(newday*300)+2500+2000
	print("the rent is :",rent)	