while True:


    s = input()
    if s=="END":
        break
    r = ''
    for c in s.strip():
        if c not in ' ':
            r = r + c
    print(r)


