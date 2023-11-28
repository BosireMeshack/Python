def power(x: int, n: int) -> int:
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)
def main():
    x = int(input("x = "))
    n = int(input("n = "))
    print(power(x, n))

if __name__ == "__main__":
    main()



