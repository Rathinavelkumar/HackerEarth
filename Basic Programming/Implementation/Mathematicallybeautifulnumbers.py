tc = int(input())
for each in range(tc):
    x, k = map(int, input().split())
    flag = True
    while x > 0:
        if x % k >= 2:
            print("NO")
            flag=False
            break
        else:
            x = x//k
    
    if flag==True: print("YES")