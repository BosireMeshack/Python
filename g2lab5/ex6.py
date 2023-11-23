ls = []
for i in range(5):
    ls.append(input("Give a fruit:\n"))

print(ls)

#list comprehension
newlist = [string.upper() for string in ls if 'a' in string]
print(newlist)