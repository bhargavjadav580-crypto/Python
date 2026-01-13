# 7. Hospital Billing System
# Charges based on stay duration:
# | Days Admitted | Cost per Day |
# |----------------|--------------|
# | 1–3 | ₹2000 |
# | 4–7 | ₹1800 |
# | 8+ | ₹1500 |
# Add ₹500 for registration + medicine charges.

day=float(input("enter the days :"))

if (day>=1 and day<=3):
	cost=day*2000

elif(day>=4 and day<=7):
	newday=day-3
	cost=(newday*1800)+6000

else:
	newday=day-7
	cost=(newday*1500)+6000+7200

totalcharge=cost+500
print("totalcharge after registration and medicine charge",totalcharge)	
