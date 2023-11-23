n = int(input("Input the range of your numbers: \n"))
num = int(input("Give the numbers you want to get maximum from: \n"))

max = num

for i in range(n-1):
    num = int(input("Input an integer: \n"))
    if num > max:
        max = num

print(max)