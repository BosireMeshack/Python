occurence = {}

word = input("Give a word: \n")

while word != "":
    if word in occurence:
        occurence[word.lower()] += 1
    else:
        occurence[word.lower()] = 1
    word = input()

for word, item in occurence.items():
    print(f"{word}:{item} item")
