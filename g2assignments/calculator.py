
print("Please choose an operator from the ones indicated below \n  + for summation \n - for subtraction \n"
           "* for multiplication \n // for division \n % for modulus \n")
op = input("Input operator: \n")

if op == '+':
    user_inputs = input("Input values separated by a space\n")

    user_values = user_inputs.split()
    length = len(user_values)
    sum = 0
    product = 1
    for i in range(length):
        user_values[i] = float(user_values[i])
        sum += user_values[i]
        product *= user_values[i]

    if op == '+':
        print("{} is the sum of {}".format(sum, user_values))
    elif op == '*':
        print("{} is the product for {}".format(product, user_values))

elif op == '-' or '/' or '%':
    values = input("Kindly input two values separated by a space\n")
    entered_values = values.split()
    if len(entered_values) < 2:
        for i in range(len(entered_values)):
            entered_values[i] = float(entered_values[i])
        entered_values.sort(reverse=True)

        print("{} - {} = {}".format(entered_values[0], entered_values[1], (entered_values[0] - entered_values[1]) ) )










