import sys

# for s in sys.stdin:
#     r=''.join([c for c in s if c.lower() not in "aeiou"])
#     print(r)

while True:
    try:
        s = input()
        r = ''.join([c for c in s if c.lower() not in "aeiou"])
        print(r)
    except EOFError:
        break
