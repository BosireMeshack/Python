n = int(input("Give a number: \n"))

answer = []


for i in range(n):
    answer.append(i+1)
    answer[i] = str(answer[i])

for w in range(len(answer)):
    if (w+1)%15 == 0:
         answer[w] = "FizzBuzz"
    elif (w+1)%5 == 0:
        answer[w+1] = "Buzz"
    elif (w+1)%3 == 0:
        answer[w] = "Fizz"
print(answer)


