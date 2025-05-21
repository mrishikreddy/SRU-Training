arr = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15]]

sele = 7

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if sele == arr[i][j]:
            print("Element found at index(row,column): (",i,j,")")
            exit(0)
print("element not found in the matrix")