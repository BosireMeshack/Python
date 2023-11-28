# Sets in python
import random
def generate_set(n:int,m:int)->set:
    set1 = set()
    set2 = set()
    i=0
    x=0
    while i <= n:
         set1.add(random.randint(1,20))
         i=i+1
    while x <= m:
        set2.add(random.randint(1,20))
        x+=1
    return set1, set2, set1&set2, set1|set2, set1-set2, set1^set2

def main()-> None:
    n = int(input("n = "))
    m = int(input("m = "))
    print(generate_set(n,m))

if __name__ == "__main__":
    main()


