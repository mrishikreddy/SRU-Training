arr = [2,5,8,6,3,1,9,4,7] 

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if not flag:
        break
print(arr)



# Below is the code where actual code logic resides, above code is to show sorted array to increase clarity
k = 10
arr = [2,5,8,6,3,1,9,4,7]   
for i in range(len(arr)):
    if i==k-1:
        break
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = True
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if not flag:
        break

if k<len(arr):
    print(arr[-k])
else:
    print("The array length is insufficient")









k = 10
arr = [2,5,8,6,3,1,9,4,7]   
for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = True
            arr[j],arr[j+1] = arr[j+1],arr[j]
    k-=1
    if not flag or k==0:
        break

if k<len(arr):
    print(arr[-k])
else:
    print("The array length is insufficient")
