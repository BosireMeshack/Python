n = int(input("Number of input: \n"))
c = 0

for i in range(n):
    try:
        a = int(input("Give a number: \n"))
        if a > 0 and a % 2 ==0:
            c+=1
    except(ValueError):
        print('Give a real number\n')
print("The number of positive and even numbers is {}".format(c))
