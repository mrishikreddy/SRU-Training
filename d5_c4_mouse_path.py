arr = [[1,0,0,0,0],
       [1,1,1,1,1],
       [1,0,1,0,1],
       [1,1,1,1,1],
       [1,1,1,0,1],]

def find_path(i,j):
    if i==len(arr)-1 and j==len(arr[0])-1:
        return 1
    elif i >= len(arr) or j >= len(arr[0]) or arr[i][j] == 0:
        return 0
    return find_path(i,j+1) + find_path(i+1,j)

print("The number of possible paths are: "find_path(0,0))