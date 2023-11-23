import sys
def generate_lists() -> list[list[int]]:
    list_of_lists = []
    for line in sys.stdin:
        tokens = line.strip().split(' ')
        list_of_lists.append([e for e in tokens])
    return list_of_lists


for ls in generate_lists():
    print(ls)