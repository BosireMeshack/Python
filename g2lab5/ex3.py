import random

random_number = random.randint(1, 10)

# while random_number!= 5:
#     print(random_number)
#     random_number = random.randint(1, 10)
# print(random_number)
i = 0
while True:
    print(random_number)
    i+=1
    if random_number== 5:
        print("Steps = ", i)
        break
    random_number = random.randint(1, 10)