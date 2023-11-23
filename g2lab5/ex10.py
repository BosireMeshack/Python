import random
ls = []
while len(ls) < 10:
    random_number = random.randint(1, 10)
    if random_number % 2 == 0:
        ls.append(random_number)

print(ls)
