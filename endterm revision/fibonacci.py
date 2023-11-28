def n_sum(n:int)->int:
    if n==1:
        return 1
    else:
        return n+n_sum(n-1)

def main()->None:
    n = int(input('n='))
    print(n_sum(n))

if __name__ == "__main__":
    main()
