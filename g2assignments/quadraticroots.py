import math

print("Enter the co-efficients of a quadratic equation \n")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x1 = ((-1*b) + math.sqrt(b**2 - 4*a*c))/2*a
x2 = ((-1*b) - math.sqrt(b**2 - 4*a*c))/2*a



print(x1,x2)