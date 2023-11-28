import sys
number_of_fests = {}
for line in sys.stdin:
    festivals = line.split(":")
    bands = festivals[1].split(",")

    print(festivals)
    for x in range(len(bands)):
        bands[x] = bands[x].strip()

    print(bands)
    for i in range(0, len(bands)):

        if bands[i] in number_of_fests:
            number_of_fests[bands[i]]+=1
        else:
            number_of_fests[bands[i]] = 1
for key in sorted(number_of_fests):
    print("{0}:{1}".format(key, number_of_fests[key]))

