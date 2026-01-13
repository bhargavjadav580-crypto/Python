# 9. Amusement Park Entry Fee
# Entry fee based on age:
# | Age Group | Fee |
# |-----------|---------|
# | < 5 | Free |
# | 5–12 | ₹50 |
# | 13–59 | ₹100 |
# | 60+ | ₹70 |

age=float(input("enter the age :"))

if age<5:
	print("fee is :free")

elif (age>=5 and age<=12):
	print("fee is :50 rupees")

elif (age>=13 and age<=59):
	print("fee is :100 rupees")
	
else:
	print("fee is :70 rupees")