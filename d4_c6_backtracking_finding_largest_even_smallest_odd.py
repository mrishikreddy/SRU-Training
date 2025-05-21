small, large = float('inf'), - float('inf')
def find_subset(small, large , l, ind):
    if ind<len(l):
        if l[ind] % 2 == 0:
            if large < l[ind]:
                large = l[ind]
        else:
            if small > l[ind]:
                small = l[ind]
        return find_subset(small, large, l , ind+1)
    return small, large
    
    

l = list(map(int,input("Enter the elements: ").split(" ")))
small, large = find_subset(small, large ,l, 0)
print(small, large)