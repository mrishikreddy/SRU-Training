nums = [2,2,4,4,6,8,8,9,9]
left = 0
right = len(nums)-1
mid = -1

while left<=right:
    mid = left + ((right -left)>>1)
    if mid%2==1:
        mid -= 1
    if nums[mid] == nums[mid+1]:
        left = mid+2
    else:
        right = mid-1

print(nums[left])