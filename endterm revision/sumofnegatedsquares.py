
def sumofnegatedsquares(n:int)->int:
    if n == 3:
        return 7
    else:
        return n*n-2+sumofnegatedsquares(n-1)


def main()->None:
    n = int(input('n='))
    sum = sumofnegatedsquares(n)

    print("sum of {}^2-2 = {}".format(n, sum))


if __name__ == "__main__":
    main()