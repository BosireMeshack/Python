string = input("Give two numbers separated by space \n")

list_of_string = string.split(' ')
a = int(list_of_string[0])
b = int(list_of_string[1])
# gcd = 1
# for i in range(2, max(a,b)):
#     if (a%i == 0 and b%i==0):
#         gcd = i
while b!=0:
    r = a % b
    a = b
    b = r


lcm = (int(list_of_string[0]) * int(list_of_string[1])// a)

print(lcm)
