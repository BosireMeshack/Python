c=0
while True:
    a = input("Give a multi-digit number:\n")

    list_of_strings = a.strip()

    ls = [int(x) for x in list_of_strings]

    for b in ls:
        if b%2 == 0:
            c+=b
        elif b == 0:
            print(c)
            break











