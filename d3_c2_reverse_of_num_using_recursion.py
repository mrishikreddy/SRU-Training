def reverse(num,ans=0):
    if num == 0:
        return ans
    ans = ans*10 + num%10
    return reverse(num//10,ans)
print(reverse(153))