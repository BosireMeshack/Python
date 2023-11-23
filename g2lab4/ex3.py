
sum = 0
count_even = 0
count_odd = 0
while True:
    a = int(input("Give a number:\n"))
    if a % 2 == 0:
        count_even+=1
    else:
        count_odd+=1
    sum+= a
    if sum > 100:
        break
print("The sum is {}. There are {} even numbers and {} odd numbers".format(sum, count_even,count_odd))

