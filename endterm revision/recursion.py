

def sum_rec(n:int)->int:
    if n == 2:
        return -22
    else:
        return -n*(n+9) + sum_rec(n-1)


def main()-> None:
    n = int(input("Enter a number:\n"))
    ls = []
    while True:
        if n == 0:
            break
        else:
            ls.append(sum_rec(n))

        n = int(input("Enter a number"))
    print(ls)

if __name__ == "__main__":
    main()