import sys
def count_of_squares(ls:list[int])->int:
    c = 0
    for e in ls:
        if int(e**(1/2)) == e**(1/2):
            c+=1
    return c

def main()-> None:
    ls = []
    for n in sys.stdin:
        ls.append(int(n))
        print(ls)
    print("The number of square elements in the list is {}".format(count_of_squares(ls)))



if __name__ == "__main__":
    main()
