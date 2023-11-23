import math

# a = int(input("Give a number \n"))
#
# gd = 1
# b = math.ceil(math.sqrt(a))
# for i in range(1, b+1):
#     if a % i == 0:
#         gd = i
# if gd != 1:
#     print(a, 'is not a prime')
# else:
#  print(a, "is prime")
c = int(input("Give a number \n"))

gd = 1
b = math.ceil(c/2)
for i in range(1, b + 1):
    if c % i == 0:
        gd = i
print('{} greatest divisor is {}'.format(c, gd))

