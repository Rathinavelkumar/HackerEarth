T = int(input())
arr = [ int(x) for x in input().split() ]

target=int(input())
for _ in range(target):
    num = int(input())

    flag=False
    total=0
    count=0

    for each in arr:
        total=total+each
        count=count+1
        if total>=num:
            flag=True
            break
        
    print(count) if flag==True else print(-1)