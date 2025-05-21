s = "aaabbaaaacccddeff"
left = 0
for right in range(1,len(s)):
    if s[right]!=s[right-1]:
        print(s[right-1],":",right-left,end=" ")
        left = right
print(s[-1],":",len(s)-left)