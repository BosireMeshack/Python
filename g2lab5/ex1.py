string = input("Give two numbers separated by a space: \n")

list_of_string = string.split(' ')
a = int(list_of_string[0])
b = int(list_of_string[1])
print(a, b)
while b != 0:
    r = a % b
    a = b
    b = r

print("The GCD is {}".format(a))
# Check if two numbers are relative primes

if a == 1:
    print("yes")
else:
    print("no")



# gcd = 1
# # if a < b:
# #     c = a
# # else:
# #     c = b
# for i in range(2, max(a,b)):
#     if(a%i==0 and b%i ==0):
#         gcd = i
# print(gcd)
