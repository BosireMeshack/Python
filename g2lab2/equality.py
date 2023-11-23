a = int(input("Enter a number:\n"))
b = int(input("Input another number:\n"))

if a == b:
    print("{} is equal to {}".format( a, b))
elif a < b:
    print("{} is smaller than {}".format(a, b))
else:
    print("{} is greater than {}". format(a, b))

