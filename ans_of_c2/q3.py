# 3. Shopping Discount Calculator
# Calculate discount based on purchase amount:
# | Amount | Discount |
# |----------------|--------------|
# | ₹5000 or more | 20% |
# | ₹3000 – ₹4999 | 15% |
# | ₹1000 – ₹2999 | 10% |
# | Below ₹1000 | No Discount |

amt=float(input("enter the amount :"))

if amt<1000:
	discount=amt*0
	print("discount is :",discount)

elif (amt>=1000 and amt <=2999):
	discount=(amt*0.1)
	print("discount is  :",discount)

elif (amt>=3000 and amt<=4999):
	newamt=amt-2999
	discount=(newamt*0.15)+199.9
	print("discount is :",discount)
	
else:
	newamt=amt-4999
	discount = (newamt*0.2)+199.9+299.85
	print("discount is :",discount)
