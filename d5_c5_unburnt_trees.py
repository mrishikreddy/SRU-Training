arr = [[0,0,0,1,1,1],
       [1,1,1,0,0,0],
       [0,0,1,1,1,1],
       [1,1,1,0,0,0],
       [0,0,0,0,0,1],
       [1,0,0,1,0,0]]

def burn_trees(i,j):
    if i >= 0 and i<len(arr) and j >= 0 and j<len(arr[0]):
        if arr[i][j] == 0:
            return
        arr[i][j] = 0
        burn_trees(i,j+1)
        burn_trees(i,j-1)
        burn_trees(i+1,j)
        burn_trees(i-1,j)
    return
        


# burn_trees(2,5)
burn_trees(5,3)
count = 0
for i in arr:
    count += sum(i)
            

print("The number of unburnt trees are: ", count)