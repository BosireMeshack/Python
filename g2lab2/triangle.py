
sides = input("Enter three numbers separated by space: ")

user_sides = sides.split()

maximum_lengths = 3
user_length = len(user_sides)
sum_of_sides = 0
if user_length != maximum_lengths:
    print("Attention, kindly input 3 numbers!")
else:

    for value in range(len(user_sides)):
        user_sides[value] = float(user_sides[value])

        user_sides.sort()
        sum_of_sides = user_sides[0] + user_sides[1]

        if sum_of_sides > user_sides[2]:
            print("The triangle is valid!")
        else:
            print("The triangle is invalid!")










