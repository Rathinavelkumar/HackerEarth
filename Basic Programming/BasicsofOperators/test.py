import math

tc = int(input())
for _ in range(tc):
    data = int(input())
    ref = int(math.sqrt(data))
    i=1
    while(i<=ref):
        temp=i
        i=i*2
    for i in range(temp,ref+2)[::-1]:
        if len(bin(i)) < len(bin(data//i)):
            break
        temp=data+1-i
    print(temp)