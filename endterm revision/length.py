import sys

streets = {}

with open(sys.argv[1]) as file:
    for line in file:
        data = line.split(";")

        if data[0] in streets:
            streets[data[0]] +=float(data[2])

        else:
            streets[data[0]] = float(data[2])

    print(streets)