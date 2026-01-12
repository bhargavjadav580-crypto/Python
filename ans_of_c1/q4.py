# Write a program that calculates income tax based on these brackets:
# Up to $10,000: 5%, $10,001-$50,000: 10%, $50,001-$100,000: 15%, Above $100,000:
# 20%

income = float(input("Enter your income: "))

if income <= 10000:
    tax = income * 0.05

elif income <= 50000:
    tax = (10000 * 0.05) + (income - 10000) * 0.10

elif income <= 100000:
    tax = (10000 * 0.05) + (40000 * 0.10) + (income - 50000) * 0.15

else:
    tax = (10000 * 0.05) + (40000 * 0.10) + (50000 * 0.15) + (income - 100000) * 0.20

print("Income Tax =", tax)
