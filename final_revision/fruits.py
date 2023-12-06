import sys

child_fruit = {}
for line in sys.stdin:
    data = line.split(":")
    names = data[0]
    fruits_count = len(data[1].split(","))

    for x in range(len(data)):
        if names in child_fruit:
            child_fruit[names] = fruits_count
        else:
            child_fruit[names] = 0
for key, value in sorted(child_fruit.items(), key = lambda x:(x[0], x[1])):
    print(f"{key}: {value} fruits")

