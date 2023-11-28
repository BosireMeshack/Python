# this function takes in a list of integers and returns integers which are squares
import random
import sys

def squares(ls:list[int])->list:

    squarelist = []
    for number in ls:
        if number == int(number**0.5)**2:
            squarelist.append(number)
    return squarelist


# Reads until end of file
# def main()-> None:
#     for line in sys.stdin:
#         numbers = line.split(" ")
#         ls = [int(number) for number in numbers]
#         s = squares(ls)
#         print(s)

# if __name__ == "__main__":
#     main()


########################################################
# Runs n times

# def main() ->None:
#     n = int(input("n="))
#     for i in range(n):
#         value = input("Give numbers separated by space:")
#         numbers = value.split(" ")
#         ls = [int(number) for number in numbers]
#         s = squares(ls)
#         print(s)
#
#
# if __name__ == "__main__":
#     main()


###############################################################
# Reads until empty line

def main()->None:
    for line in sys.stdin:
        if line.strip() == "":
            break;
        numbers = line.split(" ")
        ls = [int(number) for number in numbers]
        s = squares(ls)
        print(s)



if __name__ == "__main__":
    main()
