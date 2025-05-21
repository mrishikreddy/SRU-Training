res = float('inf')
def find_subset(res,l,target,ind=0,count=0):
    if ind == len(l):
        if target == 0:
            if res > count:
                res = count
        return res
    if l[ind] <= target:
        res = find_subset(res,l,target-l[ind],ind+1,count+1)
    res = find_subset(res,l,target,ind+1,count)
    return res

l = list(map(int,input("Enter the elements: ").split(" ")))
target = int(input("Enter the target: "))
res = find_subset(res,l,target)
if res == float('inf'):
    print("-1")
else:
    print(res)