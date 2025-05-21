arr = [5,2,3,8,1,6,7]
k = 2

for i in range(k,len(arr)-k):
    for j in range(k,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)



# efficient case:

arr = [5,2,3,8,1,6,7]
k = 2
for i in range(k,len(arr)-k):
    flag = False
    for j in range(k,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if not flag:
        break
print(arr)