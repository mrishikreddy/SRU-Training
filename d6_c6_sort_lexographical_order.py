arr = ["he", "car", "apples", "hello"]

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if not flag:
        break   
print("sorted array: ",arr)


arr = ["cet","cat","car","cap"]

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        for z in range(2):
            if ord(arr[j][z])>ord(arr[j+1][z]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
                break
    if not flag:
        break

print("sorted array: ",arr)