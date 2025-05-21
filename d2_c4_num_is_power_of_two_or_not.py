num = int(input("enter a number: "))

for i in range(32):
    if (1<<i) == num:
        print("Yes")
        exit(0)
print("No")



# Method 2

if num & (num-1) == 0:
    print("Yes")
else:
    print("No")




# Method 3

while num != 1:
    if num /2 != num //2:
        break
    num  /= 2
if num ==1:
    print("Yes")
else:
    print("No")