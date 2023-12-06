import sys

with open(sys.argv[1]) as file:
    amounts = {}
    for line in file:
        data = line.strip("\n").split(";")
        if data[1] in amounts:
            amounts[data[1]] += int(data[3])
        else:
            amounts[data[1]] = int(data[3])

    for key, value in sorted(amounts.items(), key = lambda x: ( -x[1])):
        print(f"{key} ({value} EUR)")

        # if data[0] in amounts:
        #     amounts[data[0]] += int(data[3])
        # else:
        #     amounts[data[0]] = int(data[3])

# for key, value in sorted(amounts.items(), key = lambda x:(-x[1], x[0])):
#     print(f"{key}:{value}")






