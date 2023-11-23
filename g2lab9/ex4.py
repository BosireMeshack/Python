import sys

def is_prime(a:int)->bool:
    if a == 1:
        return False
    if a == 2:
        return True
    for i in range(2, int(a**(1/2))+1):
        if a % i == 0:
            return False
    return True



def count_of_prime(ls:list[int])->int:
    c = 0
    for e in ls:
        if is_prime(e):
            c+=1
    return c
def main()-> None:
    f_out = open('out.txt','a')
    ls = []
    for e in sys.argv[1:]:
        ls.append(int(e))
    print(count_of_prime(ls), file=f_out)

if __name__ == "__main__":
    main()