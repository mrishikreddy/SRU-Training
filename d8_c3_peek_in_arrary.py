arr = [2,3,4,6,3,2,1,5,8,10,1,4,2]
left = 0
right = len(arr) - 1
while left<=right:
    mid = left + ((right - left) >> 1)
    if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
        print(arr[mid])
        exit(0)
    if arr[mid]>arr[mid+1]:
        right = mid
    else:
        left = mid + 1