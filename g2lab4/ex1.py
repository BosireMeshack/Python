c = 1
sum = 0
while c <= 10:
     a = int(input("Give a number\n"))
     c+=1
     if a % 2 != 0:
         continue
     sum += a
print(sum)

