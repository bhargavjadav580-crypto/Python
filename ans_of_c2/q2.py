# 2. Auto/Taxi Fare Calculation
# Calculate fare based on distance traveled:
# | Distance (km) | Rate per km |
# |----------------|--------------|
# | Up to 3 km | ₹15 |
# | 4 to 10 km | ₹12 |
# | Above 10 km | ₹10 |

km=float(input("enter the km :"))

if km<=3:
	rate=km*15
	print("the rate is :",rate)

elif (km>=4 and km<=10):
	newkm=km - 3
	rate=(newkm*12)+45
	print("the rate is :",rate) 
	
else:
	newkm=km - 10
	rate=(newkm*10)+45+84

	print("the rate is :",rate)	