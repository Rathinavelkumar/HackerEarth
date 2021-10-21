X, Y, S, T = map(int, input().split())

count=0
for i in range(S+1):
    for j in range(S+1):
        if X+Y+j<=T:
            count=count+1
    X=X+1
print(count)