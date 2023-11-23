
a = int(input("Give a number(exit with 0)\n"))
count_p = 0
count_n = 0

while a != 0:
    if a >= 0:
        count_p+=1
    else:
        count_n+=1
    a = int(input("Give a number(exit with 0)\n"))
print("There are {} positive numbers and {} negative numbers".format(count_p,count_n))
