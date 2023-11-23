n = int(input("Give a number:\n"))

fourth_root = n ** (1 / 4)

f = int(fourth_root)

rem = fourth_root - f
print(fourth_root)
if rem == 0:
    print('True')
else:
    print("False")
