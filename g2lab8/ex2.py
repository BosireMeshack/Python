from ex1 import count_of_squares

def main()-> None:
    n = int(input("Number of test cases:\n"))

    for _ in range(n):
        ls = []
        while True:
            n = input()
            if n == '':
                break
            ls.append(int(n))
        print(ls, count_of_squares(ls))
if __name__ == "__main__":
    main()