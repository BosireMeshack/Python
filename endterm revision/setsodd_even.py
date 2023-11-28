import random
even = set()
odd = set()
n = int(input("n = "))
m = int(input("m = "))
while len(even) < n:
    num = random.randint(1, 20)
    if num % 2 == 0:
        even.add(num)
while len(odd) < m:
    num = random.randint(1, 20)
    if num % 2 == 1:
        odd.add(num)
print(even)
print(odd)
print("Union =", even.union(odd))