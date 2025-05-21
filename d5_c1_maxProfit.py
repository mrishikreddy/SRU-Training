arr = [2,4,1,5,8,4,7]
profit = 0
day = arr[0]
for i in range(1,len(arr)):
    if day > arr[i]:
        day = arr[i]
    profit = max(profit, arr[i]-day)
print("Profir is: ", profit)