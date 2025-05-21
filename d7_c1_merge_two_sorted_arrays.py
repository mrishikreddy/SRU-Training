arr1 = [2,4,5,8,9]
arr2 = [3,5,6,9,11,12,13]

nd1,nd2 = len(arr1), len(arr2)
i = j = 0
res = []

while i<nd1 and j<nd2:
    if arr1[i]<=arr2[j]:
        res.append(arr1[i])
        i+=1
    else:
        res.append(arr2[j])
        j+=1

while i<nd1:
    res.append(arr1[i])
    i+=1
while j<nd2:
    res.append(arr2[j])
    j+=1
print("The sorted list is: ",res)