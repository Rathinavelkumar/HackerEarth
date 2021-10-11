tc = int(input())

for _ in range(tc):
    m, n = map(int, input().strip().split())

    arr=[list(input()) for i in range(m)]

    borderList=[]

    for i in range(0,m):
        top, bottom = 0, 0
        topMax, bottomMax = top, bottom

        if m==1:
            borderList.append(str(arr[i]).count("#"))
            break

        for j in range(0,n):

            if i==0 and arr[i][j]=="#" and m!=1: 
                top = top+1 
                if arr[i+1][j]==".":
                    bottom=bottom+1
                elif bottomMax<bottom: 
                    bottomMax=bottom
                    bottom=0
            elif i==0 and j==n-1:
                if bottomMax<bottom: bottomMax=bottom 
                borderList.append(max([top, bottomMax]))

            if i==m-1 and arr[i][j]=="#" and m!=1: 
                bottom=bottom+1
                if arr[i-1][j] ==".": 
                    top=top+1
                elif topMax<top:
                    topMax=top
                    top=0
            elif i==m-1 and j==n-1:
                if topMax<top: topMax=top
                borderList.append(max([topMax, bottom]))

            if i!=0 and i!=m-1 and arr[i][j]=="#" and m!=1:
                if arr[i-1][j]==".": 
                    top=top+1
                elif topMax<top:
                    topMax=top
                    top=0
                if arr[i+1][j]==".": 
                    bottom=bottom+1
                elif bottomMax<bottom: 
                    bottomMax=bottom
                    bottom=0
            elif i!=0 and i!=m-1 and j==n-1:
                if topMax<top: topMax=top       
                if bottomMax<bottom: bottomMax=bottom 
                borderList.append(max([topMax, bottomMax]))

    print(max(borderList))