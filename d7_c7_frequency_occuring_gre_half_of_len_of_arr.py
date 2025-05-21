# Boyer-Moore Majority Voting Algorithm

arr = [3,3,3,3,2,4,6]
count = 0
res = 0
for i in arr: 
    if count == 0:
        res = i
        count = 1
    elif i == res:
        count += 1
    else:
        count -=1
print(res)