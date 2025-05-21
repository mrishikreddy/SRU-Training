def xoring(num):
    if num%4==0:
        return num
    elif num%4==1:
        return 1
    elif num%4==2:
        return num+1
    elif num%4==3:
        return 0

a = 3
b = 10

print( xoring(b)^xoring(a-1))  # finding xor upto 10 and deleting xor upto 4