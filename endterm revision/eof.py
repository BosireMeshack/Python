# Reading till end of file

import sys

for line in sys.stdin:
    numbers = line.split(" ")
    lists = []

    for number in numbers:
        lists.append(int(number))
    print(lists)