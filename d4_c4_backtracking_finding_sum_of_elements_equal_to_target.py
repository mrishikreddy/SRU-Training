def find_subset(l,target,ind=0,temp=[]):
    if ind == len(l):
        if target == 0:
            print(temp)
        return
    if l[ind] <= target:
        find_subset(l,target-l[ind],ind+1,temp+[l[ind]])
    find_subset(l,target,ind+1,temp)

l = list(map(int,input("Enter the elements: ").split(" ")))
target = int(input("Enter the target: "))
find_subset(l,target)