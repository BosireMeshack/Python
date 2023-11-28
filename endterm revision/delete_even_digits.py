import sys
#Function that deletes even digits

def delete_even_digits(sls:list[int])->list:
    odd =[]
    for s in sls:
        if s%2 !=0:
            odd.append(s)
    for o in range(len(odd)):
        odd[o] = str(odd[o])
    return odd
##################################################
# This function deletes even characters
def delete_even_digits2(original: str) -> str:
    return"".join([o for o in original if o not in "02468"])


def main()->None:

    for line in sys.stdin:
        # numbers = line.strip().split(" ")
        # ls = [int(number) for number in numbers]
        odd = delete_even_digits2(line.strip())
        print(odd)

if __name__ == "__main__":
    main()




