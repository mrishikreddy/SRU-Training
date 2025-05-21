arr = [[4,13,12], [8,10,5], [7,9,20], [14,8,3]]
hmp = {}

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

for i in range(len(arr)):
    for k in range(3):
        if is_prime(arr[i][k]):
            hmp[i] = k
            break

for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        ind1 = ind2 = None
        if arr[j][hmp[j]]>arr[j+1][hmp[j+1]]:
            flag = True
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if not flag:
        break

print("sorted array: ",arr)