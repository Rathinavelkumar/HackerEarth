import math

tc = int(input())
for _ in range(tc):
    data = int(input())
    ref = int(math.sqrt(data))
    i=1
    while(i<=ref):
        i=i*2
        if data//i >= i//2:
            result = data-data//i
        else:
            result = (data-(i//2)) + 1
    print(result)