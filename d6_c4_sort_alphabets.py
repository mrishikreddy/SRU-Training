arr = ['c','b','a','d','g','f','e']

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if ord(arr[j]) > ord(arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if not flag:
        break
    
   
print("sorted array: ",arr)