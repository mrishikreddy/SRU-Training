arr = [5,4,5,5,2,5,4,3,3,3,4,2,1,1,2,1]
d = {}
max_occ = 0

for i in arr:
    if i in d:
        d[i] += 1
        max_occ = max(max_occ,d[i])
    else:
        d[i] = 1

bucket = [[] for _ in range(max_occ+1)]


for k in d:
    bucket[d[k]].append(k)

ans = []
for i in range(len(bucket)):
    for j in bucket[i]:
        ans.extend([j]*i)
print(ans)