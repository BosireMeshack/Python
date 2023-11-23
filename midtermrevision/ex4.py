import sys

for s in sys.stdin:
    s = s.strip()
    i = 0
    while i < len(s):
        if s[i].lower() in 'aeiou':
            s = s.replace(s[i],'')
        i = i+1
    print(s)
