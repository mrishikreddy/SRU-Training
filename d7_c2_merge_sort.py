def merge(arr):
    if len(arr)>1:     
        left_arr = arr[:len(arr)//2]   
        right_arr = arr[len(arr)//2:]
        merge(left_arr)
        merge(right_arr)

        i=j=k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            k+=1
            i+=1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            k+=1
            j+=1
        

arr = [2,5,6,7,4,1,3]
merge(arr)
print("Sorted array: ", arr)