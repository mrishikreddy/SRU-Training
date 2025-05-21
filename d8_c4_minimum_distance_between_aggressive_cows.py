# def aggressiveCows(stalls, target):
#         res = float('inf')
#         mini = 1
#         while True:
#             prev = stalls[0]
#             k = target - 1
#             for i in stalls[1:]:
#                 if i - prev >= mini:
#                         prev = i
#                         k -= 1
#             if(k<=0):
#                 mini += 1
#             else:
#                 break
#         print(mini-1)
# aggressiveCows([1,2,4,8,9], 3)



def aggressiveCows(stalls, target):
        stalls.sort()
        left = 1
        right = stalls[-1] - stalls[0]
        while left<=right:
            mid = left + ((right-left)>>1)
            prev = stalls[0]
            k = target - 1
            for i in stalls[1:]:
                if i - prev >= mid:
                        prev = i
                        k -= 1
            if(k<=0):
                left = mid + 1
            else:
                right = mid - 1
        return right

aggressiveCows([1, 2, 3, 20], 3)