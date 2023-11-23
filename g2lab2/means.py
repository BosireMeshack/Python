from typing import List

user_input = input("Enter a list of numbers separated by space \n")

user_values = user_input.split()

for value in range(len(user_values)):
    user_values[value] = float(user_values[value])
summation = 0
geometric =1



for i in range(len(user_values)):

    summation += user_values[i]
    geometric *= user_values[i]

print(summation)



print("{} is the arithmetic mean of {}".format(summation//len(user_values), user_values))
print("{} is the geometric mean of {}".format(geometric**(1/len(user_values)), user_values))

