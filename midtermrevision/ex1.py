count = 0

a = input("Enter a number: \n")
b = a.split()
print(b)

c = [int(x) for x in b]

# print(len(c),c)
for i in c:
 if i > 0 and i%2 == 0:
    count+=1
print(count)
