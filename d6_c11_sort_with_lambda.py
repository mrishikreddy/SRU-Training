arr = [[4,13,12], [8,10,5], [7,9,20], [14,8,3]]
hmp = {}

def find_prime(l):
    ind = None
    for num in l:
        if num<2:
            continue
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                break
        else:
            return num
    return float('inf')

arr.sort(key=find_prime)   
print("sorted array: ",arr)