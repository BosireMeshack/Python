import sys

def count_of_odds(ls:list[int])->int:
    c = 0
    for e in ls:
        if e % 2 == 1:
            c+=1
    return c

def main()->None:
    ls = []
    for e in sys.argv[1:]:
        ls.append(int(e))
    print(count_of_odds(ls))

if __name__ == "__main__":
    print(sys.argv)
    main()