a = int(input('Give a number: \n'))
i = 1
sum = 0
while i <= a:
    sum+= i
    i += 1
print(sum, a*(a+1)/2)