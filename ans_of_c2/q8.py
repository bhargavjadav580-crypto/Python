# 8. Mobile Recharge Plan
# Input plan code and print plan details:
# 1. ₹199 – 28 Days – 1.5GB/day
# 2. ₹299 – 56 Days – 2GB/day
# 3. ₹399 – 84 Days – 2.5GB/day

plancode=float(input("enter the plancode :"))

if(plancode==1):
	print("plan details is : ₹199 28days 1.5gb/day")

elif(plancode==2):
	print("plan details is : ₹299 56days 2.0gb/day")

elif(plancode==3):
	print("plan details is : ₹399 84days 2.5gb/day")
	
else:
	print("sorry print 1,2 or3")

