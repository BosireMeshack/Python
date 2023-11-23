op = input("Input one of the following operator +, -, *, /, //, %: \n")

match op:
    case '+':
        sum = 0
        counter = int(input("How many numbers do you want to add?: \n"))
        for i in range(counter):

            b = int(input("Input a number: \n"))
            sum+=b

        print(sum)
    case '-':
        a = int(input("Enter the minuend:\n"))
        b = int(input("Enter the subtrahend:\n"))
        print("The difference of {} and {} is {}".format(a,b,(a-b)))
    case '*':
        prod = 1
        counter = int(input("How many numbers do you want to multiply:\n"))
        for i in range(counter):
            b = int(input("Enter a factor:\n"))
            prod *= b
            print(prod)
    case '/':
        divident = int(input("Input the divident: \n"))
        divisor = int(input("Input the divisor: \n"))
        print("The quotient of {} / {} is {}".format(divident, divisor,(divident/divisor)))
    case "//":
        dividend = int(input("Input the dividend: \n"))
        divisor = int(input("Input the divisor: \n"))
        print("The quotient of {} // {} is {}".format(dividend, divisor,(dividend//divisor)))
    case "%":
        dividend = int(input("Input the divident: \n"))
        divisor = int(input("Input the divisor: \n"))
        print("The modulus of {} % {} is {}".format(dividend, divisor, (dividend % divisor)))

    case _:
        print("Invalid input\n")