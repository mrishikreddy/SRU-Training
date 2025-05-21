arr = [[2,3],[5,1],[1,4],[2,7],[1,3]]

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr [j][1] > arr[j+1][1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if not flag:
        break
    
   
print("sorted array: ",arr)