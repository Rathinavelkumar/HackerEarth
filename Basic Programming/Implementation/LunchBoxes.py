tc = int(input())

for each in range(0,tc):
    schools = []
    n, m = map(int, input().split(" "))
    schools = [ int(x) for x in input().split() ]
    schools.sort()

    count=0
    for i in range(m):
        n = n-schools[i]
        if n>=0:
            count = count+1
        else:
            break
        
    print(count)