# arr = [55,33,22,11,44]
# arr = [55,11,22,33,44]
arr = [3,5,1,2,4,7,9,8,3]

count = 0
for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    count += 1
    if not flag:
        break
    
   
print("sorted array: ",arr, " in ",count," passes")

# Note: count is for denoting number of passes, remove it while writing efficient bubble sort code