import sys

num_of_attractions = {}

for line in sys.stdin:
    data = line.split(":")
    city = data[0]
    attractions = len(data[1].split(","))

    for i in range(len(data)):
        if city in num_of_attractions:
            num_of_attractions[city] = attractions
        else:
            num_of_attractions[city] = 0

# sorted_attract = dict(sorted(num_of_attractions.items(), key=lambda item:item[1]))

for key, value in sorted(num_of_attractions.items(), key = lambda x: x[0]):
    print(f"{key}:{value}")

# for key, value in sorted_attract.items():
#     print(f"{key}:{value}")


