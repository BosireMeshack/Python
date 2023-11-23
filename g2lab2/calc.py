a = int(input("Give the 1st number \n"))
b = int(input("Give the 2nd number \n"))
o = input("Give an operator \n")

if o == '+':
    print("{} + {} = {}".format(a, b, a+b))
elif o == '-':
    print("{} - {} = {}".format(a, b, a-b))
elif o == '*':
    print("{} * {} = {}".format(a, b, a * b))
elif o == '/' and b != 0:
    print("{} / {} = {}".format(a,b,a/b))
elif o == '/' and b == 0:
    print("We can't divide a number by zero!")
else:
    print("Bad operator")
