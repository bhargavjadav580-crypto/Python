# Write a program that takes three sides of a triangle and determines
#  if it's:Equilateral (all sides equal), isosceles (two sides equal),
#  or scalene (no sides equal)

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if triangle is valid
if a + b > c and a + c > b and b + c > a:
    
    if a == b and b == c:
        print("Equilateral Triangle")
        
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
        
    else:
        print("Scalene Triangle")

else:
    print("Not a valid triangle")
