num = int(input("enter a number: "))
if num==1:
    print("Neither prime nor composite")
    exit(0)

for i in range(2, int(num**0.5)+1):
    if num%i==0:
        print("Not a Prime Number")
        break
else:
    if num>200:
        print("Prime number greater than 200")
    elif num==200:
        print("Prime number equal to 200")
    else:
        print("Prime number less than 200")