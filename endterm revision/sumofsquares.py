def sumsquares(n:int)->int:
    if n == 1:
        return 1
    else:
        return n ** 2  + sumsquares(n-1)


def main()->None:
    n = int(input('n='))
    sum = sumsquares(n)
    print(sum)

if __name__ == "__main__":
    main()
