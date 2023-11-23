# SETS

import random

def main()->None:
    a,b = input("Give two numbers separated by space:\n").split(' ')
    s1 = set()
    s2 = set()

    while len(s1) != int(a):
        s1.add(random.randint(1,10))

    while len(s2) != int(b):
        s2.add(random.randint(1,10))

    print(s1)
    print(s2)

    print(s1&s2)
    print(s1.union(s2))
    print(s1-s2)
    print(s1.symmetric_difference(s2))

if __name__ == '__main__':
    main()




