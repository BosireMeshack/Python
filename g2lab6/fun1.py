import random
import math

def generate(ls:list[int]) -> list[int]:

    for i in range(10):
        ls.append(random.randint(1,100))
    return ls
ls=[]
ls = generate(ls)
# print(ls)

def minimum_value(ls:list[int]) -> int:
    min_v = ls[0]
    for i in range(1,len(ls)):
        if min_v >ls[i]:
            min_v=ls[i]
    return min_v
min_v = minimum_value(ls)
# print(min_v)
#Prints the index of the maximum value/integer in a list
def maximum_index(ls:list[int]) -> int:
    max_v = ls[0]
    max_i=0
    for x in range(1,len(ls)):
        if max_v < ls[x]:
            max_v = ls[x]
            max_i = x
    return max_i
max_i = maximum_index(ls)
# print(max_i)

#Prints the number of even numbers in a list
def even(ls:list[int]) -> int:
    c = 0
    for i in ls:
        if i % 2 ==0:
            c+=1
    return c

count = even(ls)
# print(count)

def isprime(a:int)-> bool:
    if a == 1:
        return False
    if a == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(a))+1):
        if a % i ==0:
            return False
    return True

# print(isprime(25))

def count_primes(ls:list[int])->int:
    c = 0
    for e in ls:
        if isprime(e) == True:
            c+=1
    return c

primes_counter=count_primes(ls)
# print(primes_counter)

def main()->None:
    ls = generate([])
    print(ls)
    print("The minimum value of the list is {}:".format(minimum_value(ls)))
    print("The index of the maximum value is {}".format(maximum_index(ls)))
    print("The number of even values is {}:".format(even(ls)))
    print("The number of primes is {}".format(count_primes(ls)))


if __name__ == '__main__':
    main()


