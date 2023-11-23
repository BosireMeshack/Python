a = int(input('Give a number: \n'))

p= 1
i=1
while i <= a:
    p*=i
    i += 1
print('The product of the first {} number is {}'.format(a, p))