user_inputs = input("Input two values separated by a space\n")

user_values = user_inputs.split()

inputs_count = len(user_values)
sum = 0
product = 1
quotient = 0
modulus = 0

if inputs_count > 2:
    print("Strictly enter two values only!")

else:
    for i in range(inputs_count):
        user_values[i] = float(user_values[i])
    user_values.sort(reverse = True)
    for x in range(inputs_count):
        sum += user_values[x]
        product *= user_values[x]
    print("{} is the sum of {} and {}".format(sum, user_values[0], user_values[1]))
    print("{} is the product of {} and {}".format(product, user_values[0], user_values[1]))

    difference = user_values[0] - user_values[1]

    minimum = min(user_values)
    if minimum !=0:
        quotient1 = user_values[0] // user_values[1]
        quotient2 = user_values[0] / user_values[1]
        modulus = user_values[0] % user_values[1]
    else:
        print("A number can not be divided by zero!")

    print("{} is the modulus of {} and {}".format(modulus, user_values[0], user_values[1]))
    print("{} is the difference of {} and {}".format(difference, user_values[0], user_values[1]))
    print("{} is the int quotient of {} and {}".format(quotient2, user_values[0], user_values[1]))
    print("{} is the float quotient of {} and {}".format(quotient1, user_values[0], user_values[1]))



