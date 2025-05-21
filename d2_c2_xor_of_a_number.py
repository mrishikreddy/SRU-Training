def xoring(num):
    if num%4==0:
        return num
    elif num%4==1:
        return 1
    elif num%4==2:
        return num+1
    elif num%4==3:
        return 0

print(xoring(5))