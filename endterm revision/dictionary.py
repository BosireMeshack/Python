# shoppinglist = {
#     "apple" : 2,
#     "pear" : 1,
#     "peach" :5
# }
#
# print(shoppinglist)

# shoppinglist = dict()
#
# shoppinglist['apple'] = 2
# shoppinglist['pear'] = 1
# shoppinglist['peach'] = 5
# print(shoppinglist)

shoppinglist = dict([
    ("apple", 2),
    ("pear", 1),
    ("peach", 5),
])

print(shoppinglist["apple"])
print("apple" in shoppinglist)
shoppinglist["plum"] = 7
print(shoppinglist)

try:
    print(shoppinglist["pspsjs"])
except KeyError as e:
    print("Not on it!")
