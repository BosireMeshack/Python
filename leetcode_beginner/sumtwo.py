nums = [2, 11, 7, 8,]

target = 9

output = []

w = 1
for x in range(len(nums)):

    for y in range(x+w,len(nums)):
        if nums[x] + nums[y] == target:
            output.append(x)
            output.append(y)
            w+=1
            print(output)

            break





