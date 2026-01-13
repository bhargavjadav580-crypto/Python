# 5. Sales Commission Calculator
# Commission based on sales:
# | Sales Amount | Commission Rate |
# |-------------------|------------------|
# | > ₹50,000 | 10% |
# | ₹30,000 – ₹50,000 | 7% |
# | ₹10,000 – ₹29,999 | 5% |
# | < ₹10,000 | 2% |

saleamount=float(input("enter the sale amount :"))

if saleamount<10000:
	comission=saleamount*0.02
	print("comission is :",comission)

elif (saleamount >=10000 and saleamount<=29999):
	newsaleamount=saleamount-9999
	comission=(newsaleamount*0.05)+199.98
	print("comission is :",comission)

elif (saleamount >=30000 and saleamount<=50000):
	newsaleamount=saleamount-29999
	comission=(newsaleamount*0.07)+199.98+999.95
	print("comission is :",comission)

else:
	newsaleamount=saleamount-50000
	comission=(newsaleamount*0.1)+199.98+999.85+1400
	print("comission is :",comission)