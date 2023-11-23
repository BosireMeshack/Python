def main()->None:
    line = input()
    d = {}
    while True:
        if line == '':
            break
        fruit_name = line.strip().split(':')[0]
        children = line.strip().split(':')[1].split(',')
        for child in children:
            if child not in d:
                d[child] = [fruit_name]
            else:
                d[child].append(fruit_name)
        line = input()

    for k, v in sorted(d.items(), key= lambda item: (-len(item[1]),item[0])):
        print(k, ':', len(v))

if __name__ == "__main__":
    main()