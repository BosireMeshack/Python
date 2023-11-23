i = 0
sum = 0
while i < 10:
    a = int(input("Give a number:\n"))

    if a % 2 == 1:
        i += 1
        continue
    else:
        i+=1
        sum += i

print(sum)
