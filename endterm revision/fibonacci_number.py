def fiboacci_num(n:int)->int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fiboacci_num(n-1)+fiboacci_num(n-1)



def main()->None:
    n = int(input("n="))
    fib_num = fiboacci_num(n)
    print("Fibonacci number of {} = {}".format(n, fib_num))

if __name__ == "__main__":
    main()