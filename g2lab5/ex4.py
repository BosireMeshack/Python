#Printing elements in a list
a = [i for i in range(1, 11)]
b = [x for x in a if x < 6]
print(a)
print(b)

# fruits = ['orange','banana', 'apple', 'pears', 'tomato', 'kiwi']
# newlist = [x if x != "banana" else "orange" for x in fruits ]
# print(newlist)

thislist = [100, 50, 65, 82, 23]

newlist = [n for n in thislist]

