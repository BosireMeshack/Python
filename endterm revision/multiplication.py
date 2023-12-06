import sys


def apply_multiplication(arr: list) -> list:
    factor = arr[0]
    for i in range(1, len(arr)):
        arr[i] = arr[i]*factor
    return arr


def main():
    arr = []
    for line in range(1, len(sys.argv)):
        arr.append(float(sys.argv[line]))

    result = apply_multiplication(arr)
    for i in range(1, len(result)):
        print("{:.3f},".format(result[i]), end=" ")


if __name__ == '__main__':
    main()