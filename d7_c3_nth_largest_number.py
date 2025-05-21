arr = [2,4,4,2,1,9,5,8,7,13,3]
k = 3

b = [0 for i in range(max(arr)+1)]

for i in arr:
    b[i] = 1
print(b)
i = len(b)-1

while k:
    if b[i]==1:
        k-=1
    i-=1
print(i+1)