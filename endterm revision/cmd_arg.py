import sys

argc = len(sys.argv)

# print("Number of arguments",argc)
# print("File location:", sys.argv[0])

# product of command line arguments
# p = 1
# for i in range(1, argc):
#     p*=int(sys.argv[i])
#
# print("product =", p)

# Number of odd_numbers in the command line arguments
c = 0
for i in range(1, argc):
    if int(sys.argv[i])%2 ==1:
        c+=1
print("number of odd_numbers",c)
