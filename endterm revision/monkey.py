import sys

monkey = {}

for line in sys.stdin:
    data = line.split(";")

    if data[0] in monkey:
        monkey[data[0]] += int(data[1])
    else:
        monkey[data[0]] = int(data[1])

for key in sorted(monkey):
    print("{0}:{1}".format(key, monkey[key]))