l = [7,6,5,2,1]
arr = [[0,1,1,0,1],
       [1,1,0,0,1],
       [0,0,0,1,1],
       [0,1,0,0,0],]

dec = [0]* len(arr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            dec[i] += l[j]
print(dec)