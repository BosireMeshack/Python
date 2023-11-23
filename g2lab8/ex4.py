import random

a,b = input("Give the sizes of the sets separated with space:\n").split(' ')
s1 = set()
s2 = set()

while len(s1) != int(a):
    r = random.randint(1,20)
    if r % 2 == 0:
        s1.add(r)
while len(s2) != int(a):
    r = random.randint(1,20)
    if r % 2 != 0:
        s2.add(r)

print("Even set:",s1)
print("Odd set:", s2)
print("Union:", s1.union(s2))


