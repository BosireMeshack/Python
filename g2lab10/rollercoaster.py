from typing import NamedTuple
import sys

RollerCoaster = NamedTuple('RollerCoaster', [('name', str), ('world', str),('height', int), ('time', int)])


def line_to_coaster(line:str)->RollerCoaster:
    tokens = line.strip().split(';')
    return RollerCoaster(tokens[0],tokens[1],int(tokens[2]),int(tokens[3]))




def coaster_to_line(coaster:RollerCoaster)->str:
    return '{} ({}): {}'.format(coaster.name,coaster.world, coaster.time)

# print(coaster_to_line(d))

def sort_coasters(coasters:list[RollerCoaster])->list[RollerCoaster]:
    return sorted(coasters, key=lambda coaster: (coaster.time, -coaster.height, coaster.name))


def main()->None:
    f_in=open(sys.argv[1])
    ls = []

    for line in f_in:
        ls.append(line_to_coaster(line))

    ls_sorted = sort_coasters(ls)

    for coaster in ls_sorted:
        print(coaster_to_line(coaster))

    d = {}
    for coaster in ls_sorted:
        if coaster.world not in d:
            d[coaster.world] = [coaster]
        else:
            d[coaster.world].append(coaster)
    print("#######################################################")
    for world in d:
        print(world,':')
        for coaster in d[world]:
            print(coaster_to_line(coaster))

    s = set()
    for coaster in ls:
        s.add(coaster.height)
    print(s)

if __name__ == "__main__":
    main()
