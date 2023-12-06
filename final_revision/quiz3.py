def sum_rec(ls:int)->int:
    if ls == 3:
        return -27
    else:
        return ls**2*(ls-2*ls)


def main()->None:

    lis = []
    while True:
        n = input("Enter a number")
        if n == "STOP":
            break
        else:
            n = int(n)
            lis.append(sum_rec(n))

        print(lis)

if __name__ == "__main__":
    main()


