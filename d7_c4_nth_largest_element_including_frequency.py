arr = [2,4,4,2,1,9,5,8,7,13,3]
print(sorted(arr))
k = 6

b = [0 for i in range(max(arr)+1)]

for i in arr:
    b[i] += 1
print(b)
i = len(b)-1

while i>=0:
    if b[i]:
        k-=b[i]
        if k<=0:
            break
    i-=1
print(i)