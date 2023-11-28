import sys

for line in sys.stdin:
    if line.strip() == "":
        break
    numbers = line.strip(" ")
    lists = []
    for number in numbers:
        lists.append(number)
    print(lists)