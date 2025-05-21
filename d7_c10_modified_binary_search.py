# if element is found return it's index, if not found return where should place it (while still maintaing sorted order).

arr = [2,3,5,6,7,9,10,13,15,16]
num = 8

first = 0 
last = len(arr)-1
while first<=last:          
    mid = (first+last)//2
    if arr[mid] == num:
        print("The entered nummber found at index",left)
        exit(0)
    elif arr[mid]<num:
        first = mid +1
    elif arr[mid]>num:
            last = mid-1
print("number not found insert at index: ", mid)