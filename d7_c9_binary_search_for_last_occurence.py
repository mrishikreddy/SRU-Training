# arr = [2,3,5,6,7,7,7,7,7,7,7, 8,  9,10,10,10,13,15,16]
# #      0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
# sele = 7

# first = 0
# last = len(arr)-1
# ind = None
# while first<=last:
#     mid = (first+last)//2
#     if arr[mid] == sele:
#         while mid<len(arr)-1 and arr[mid] == arr[mid+1]:
#             mid+=1
#         print("element last found at index: ",mid)
#         exit(0)
#     elif arr[mid] < sele:
#         first = mid+1
#     elif arr[mid] > sele:
#         last = mid

# print("element Not found")



# getting the 
arr = [2,3,5,6,7,7,7,7,7,8,9,10,10,10,13,15]
sele = 7

left = 0
right = len(arr)-1
res = None
while left<=right:
    mid = (left+right)//2
    if arr[mid] == sele:
        res = mid
        left = mid+1
    elif arr[mid] < sele:
        left = mid+1
    elif arr[mid] > sele:
        right = mid-1

if res:
    print("element found at index: ",res)
else:
    print("element not found in the array")