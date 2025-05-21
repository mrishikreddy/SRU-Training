arr = [ 5, 8, 9, 10, 1, 2]

left = 0
right = len(arr) - 1

if arr[left] < arr[right]:
    print("Array is not rotated")
else:
    while left <= right:
        mid = left + ((right - left) >> 1)
        if mid > 0 and arr[left] < arr[left - 1]:
            print(left)
            exit(0)
        elif arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1