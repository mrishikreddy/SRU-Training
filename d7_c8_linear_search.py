arr = [2,4,3,1,4,2,3,4,5]
sele = 4
res = -1
for i in range(len(arr)):
    if arr[i] == sele:
        res = i
if res>=0:
    print("found at index: ",res)
else:
    print("element not found")