import sys

# for line in sys.stdin:
#     print(line)

while True:
    try:
        print(input())
    except(EOFError):
        break