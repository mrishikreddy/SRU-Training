# num = 34.00000
# left,right = 1,1000
# c = 0
# mid = -1

# while left<right:
#     mid = (left+right)/2
#     c+=1
#     if c==100:
#         break
#     if mid**2 == num:
#         pass
#     elif mid**2>num:
#         right = mid
#     else:
#         left = mid

# print(mid)


num = 38
left,right = 1,num//2
while left<=right:
    mid = left + ((right-left)>>1)
    if mid**2 == num:
        print(mid)
        exit(0)
    elif mid**2>num:
        right = mid - 1
    else:
        left = mid + 1

print(left-1)