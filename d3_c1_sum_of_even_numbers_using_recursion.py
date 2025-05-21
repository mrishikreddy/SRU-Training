def sum_of_eve(arr,ind,ans):
    if ind == len(arr):
        return ans
    elif not arr[ind] & 1:
        ans += arr[ind]
    return sum_of_eve(arr,ind+1,ans)
arr = [2,5,6,7,2,1,4,3,6]
print("Sum of even numbers is: ",sum_of_eve(arr,0,0))


# method 2

def soe(arr,ind):
    if ind==len(arr):
        return 0
    return (arr[ind] if not arr[ind]&1 else 0) + soe(arr,ind+1)
print("Sum of even numbers is: ",soe(arr,0)) 