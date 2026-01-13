# 6. Petrol Bill Calculator
# Given price per liter is ₹105. Input liters filled and calculate total bill.
# If total amount > ₹1000, apply ₹50 cashback.

liter=float(input("enter the liter :"))

totalprice=liter*105
print("total price is  :",totalprice)

if totalprice>1000:
	price_after_cashback=totalprice-50
	print("priceaftercashback is :",price_after_cashback)

print("price_after_cashback is : ",price_after_cashback) 