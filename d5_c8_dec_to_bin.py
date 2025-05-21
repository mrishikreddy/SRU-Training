# num = int(input("enter a decimal number: "))
# res = []
# while num:
#     res.append(num%2)
#     num //= 2
# print(res[-1::-1])

s = ""
n = 12
count = 0
while True:
    if 2**count < n:
        count+=1
    else:
        break

a = 12
def dtb(c,s):
    if a == -1:
        return a
    if len(s) == count:
        print(s)
        a 
    c += 1
    if c == n:
        exit(0)
    dtb(c,s+"0")
    dtb(c,s+"1")
    return c
dtb(0,s)