import random
product = 1
for i in range(10):
    random_number = random.randint(1,10)
    print(random_number)
    product *= random_number
print(product)
