arr = [[1,0,0,1,1],
       [1,0,0,0,1],
       [0,0,0,1,0],
       [1,0,0,1,0],
       [1,0,0,1,1],]

visited = [[False for j in range(len(arr[0]))] for i in range(len(arr))]

def find_island(i,j):
    if i >= 0 and i<len(arr) and j >= 0 and j<len(arr[0]):
        if visited[i][j] == True or arr[i][j] == 0:
            visited[i][j] = True
            return 0
        visited[i][j] = True
        find_island(i,j+1)
        find_island(i,j-1)
        find_island(i+1,j)
        find_island(i-1,j)
        return 1
    return 0


count = 0
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if visited[r][c] == False:
            count += find_island(r, c)
print("The number of islands are: ", count)