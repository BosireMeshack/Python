import math

while True:
    try:
        a = input("Give a list of numbers separated by space:\n")
        square_counter = 0
        num = a.split()
        numb = [x for x in num]
        for y in range(len(numb)):
            numb[y] = int(numb[y])

        for w in numb:
            root = math.sqrt(w)
            if root.is_integer():

                square_counter+=1

        print(int(square_counter))
    except EOFError:

        break
















