import sys
try:
    sum = 0
    c = 0
    for l in sys.stdin:
        c+=1
        sum += int(l)

    print("The average is {}".format(sum/c))
except(ZeroDivisionError):
    print("Forgot to give a number")

