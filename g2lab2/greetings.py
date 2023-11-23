hours = int(input("How many hours?\n"))

if hours < 12:
    print("Good morning")
elif hours < 17:
    print("Good afternoon")
elif hours<22:
    print("Good evening")
else:
    print("Good night")