# 10. Income Tax Calculator
# Calculate tax on annual income:
# | Income Range | Tax Rate |
# |--------------------|----------|
# | < ₹2.5L | 0% |
# | ₹2.5L – ₹5L | 5% |
# | ₹5L – ₹10L | 10% |
# | Above ₹10L | 20% |

income = float(input("Enter annual income (in ₹): "))

if income < 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.10

else:
    tax = (250000 * 0.05) + (500000 * 0.10) + (income - 1000000) * 0.20

print("Income Tax =", tax)
