sentence = "The quick brown fox jumped over the lazy dog"

ls = [len(c) for c in sentence.split()]
new = sentence.split()
print(new)
print(ls)
num = []
for i in range(len(new)):
    count = 0
    for j in new[i]:
        count +=1
    num.append(count)
print(num)