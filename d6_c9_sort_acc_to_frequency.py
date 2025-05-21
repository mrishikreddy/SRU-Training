# arr = [4,5,4,7,3,2,2,3,1,5,6,8,9,2,1,1]
arr = [7,2,6,3,6,7,7,2,2,2]
count = {}
l = []
             
for i in arr:
    if i in count:
        count[i] += 1       
    else:
        count[i] = 1
        l.append(i)


c = 0
for i in range(len(l)):
    flag = False
    for j in range(0,len(l)-i-1):
        if count[l[j]] > count[l[j+1]]:
            l[j],l[j+1] = l[j+1],l[j]
            flag = True
    c += 1
    if not flag:
        break

for i in l:
    for j in range(count[i]):
        print(i,end=" ")



# another approach
# arr = [5,4,5,5,2,5,4,3,3,3,4,2,1,1,2,1]
# count = {}
             
# for i in arr:
#     if i in count:
#         count[i] += 1       
#     else:
#         count[i] = 1
# count = list(count.items())

# c = 0
# for i in range(len(count)):
#     flag = False
#     for j in range(0,len(count)-i-1):
#         if count[j][1] > count[j][1]:
#             count[j],count[j+1] = count[j+1],count[j]
#             flag = True
#     c += 1
#     if not flag:
#         break

# for i in count:
#     for j in range(i[1]):
#         print(i[0],end=" ")  