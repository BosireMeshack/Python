import sys


prices = {}
with open(sys.argv[1]) as file:
    for line in file:
        data = line.strip("\n").split(":")
        brand = data[0]
        for x in data:
            if brand in prices:
                prices[brand] = int(data[3])/int(data[2])
            else:
                prices[brand] = int(data[3])/int(data[2])


    for key, value in sorted(prices.items(), key = lambda x:(-x[1], x[0])):
        print(f"{key} ({value} HUF)")


