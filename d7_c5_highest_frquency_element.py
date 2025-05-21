arr = [2,4,4,2,1,9,5,8,7,13,3]
d = {}
max_occ = 0

for i in arr:
    if i in d:
        d[i] += 1
        max_occ = max(max_occ,d[i])
    else:
        d[i] = 1

for i in d:
    if d[i] == max_occ:
        print(i,end=" ")
print()