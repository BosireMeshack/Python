word = input("Type a word:\n")
word_dict = {}
while word != '':
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] +=1
    word = input("Type a word:\n")

    for key,v in word_dict.items():
        print(key,":",v)