
arr = list(input("Enter a sentence:").split(" "))
# an apple a day keeps doctor away
# a an day away apple keeps doctor
l = [len(i) for i in arr]
print(l)        


count = 0
for i in range(len(arr)):
    flag = False
    for j in range(0,len(arr)-i-1):
        if l[j]>l[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            l[j],l[j+1] = l[j+1],l[j]
            flag = True
    count += 1
    if not flag:
        break
    
   
print(" ".join(arr))