# 1. Electricity Bill Calculator
# Calculate electricity bill based on the following:
# | Units Used | Rate per Unit |
# |------------------|----------------|
# | 1 – 50 | ₹0.50 |
# | 51 – 150 | ₹0.75 |
# | 151 – 250 | ₹1.20 |
# | Above 250 | ₹1.50 |
# Add a 20% surcharge on the total bill amount.

unit=int(input("enter the unit  :"))

if(unit>=1 and unit<=50):
	bill=unit*0.50

elif(unit>=51 and unit<=150):
	newunit=unit - 50
	bill=(newunit*0.75)+(50*0.5)
	
elif(unit>=151 and unit<=250):
	newunit=unit - 150
	bill=(newunit*1.20)+(50*0.5)+(100*0.75)
else:
	newunit=unit - 250
	bill=(newunit*1.50)+(50*0.5)+(100*0.75)+(100*1.20)
 
bill = bill * 1.20  

print("total bill  is :",bill)	
