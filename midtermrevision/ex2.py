import sys

for s in sys.stdin:
    r = ''
    for c in s.strip():
        if c.lower() not in "aeiou":
            r = r+c
    print(r)

