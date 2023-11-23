
product = 1
while True:
    n = input("Give a number:\n")

    if n == '0':
        break
    for i in n:
        if int(i)%2 ==0:
            product*=int(i)
print(product)







