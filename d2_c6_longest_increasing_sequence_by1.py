maxi = 1
nums = [2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
left = 0

for right in range(1,len(nums)):
    if nums[right] != nums[right-1] + 1:
        maxi = max(maxi,right-left)
        left = right
maxi = max(maxi,len(nums)-left)

print("length of longest increasing sequence by 1 is:", maxi)


