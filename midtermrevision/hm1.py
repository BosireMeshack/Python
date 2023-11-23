import random
ls = []
random_numbers =  random.randint(1, 11)

while len(ls) <10:

    ls.append(random_numbers)
    random_numbers = random.randint(1,11)
print(ls)
sum = 0
even = []
odd = []
for i in ls:
    sum += i
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort(reverse=True)
print(sum)
print(min(ls), max(ls), even, odd)
