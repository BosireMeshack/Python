a = [[1,5],[7,3],[3,5]]

sum_accounts = []
for i in range(len(a)):
    sum = 0

    for j in range(len(a[i])):
        sum += a[i][j]

    sum_accounts.append(sum)

    if i == 0:
        print("{}st customer has wealth = {}".format(i+1, sum))
    elif i == 1:
        print("{}nd customer has wealth = {}".format(i + 1, sum))
    elif i == 2:
        print("{}rd customer has wealth = {}".format(i + 1, sum))
    else:
        print("{}th customer has wealth = {}".format(i + 1, sum))
max_value = max(sum_accounts)
max_index = sum_accounts.index(max_value)

match max_index:
    case 0:
        print("The {}st customer is the richest with a wealth of {}".format(max_index+1, max_value))
    case 1:
        print("The {}nd customer is the richest with a wealth of {}".format(max_index + 1, max_value))
    case 2:
        print("The {}rd customer is the richest with a wealth of {}".format(max_index + 1, max_value))
    case _:
        print("The {}th customer is the richest with a wealth of {}".format(max_index + 1, max_value))

# while x < len(a[i]):
    #     sum += a[i][x]
    #     x+=1
    # print(sum)

