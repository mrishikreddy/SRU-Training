arr = [2,4,4,2,1,9,5,8,7,13,3]
k = 1
d = {}
max_occ = 0

for i in arr:
    if i in d:
        d[i] += 1
        max_occ = max(max_occ,d[i])
    else:
        d[i] = 1

bucket = [[] for _ in range(max_occ+1)]
for z in d:
    bucket[d[z]].append(z)

if k<=max_occ and len(bucket[-k]):
    print(bucket[-k])
else:
    print("No elements found")