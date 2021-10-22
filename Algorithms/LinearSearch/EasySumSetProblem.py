n=int(input())
A_set = list( map(int, input().split()) )

m=int(input())
C_set = list( map(int, input().split()) )

for i in range(max(C_set)-max(A_set)+1):
    count=0
    for j in A_set:
        if i+j in C_set: count=count+1
    if(count==n): print(i, end=" ")