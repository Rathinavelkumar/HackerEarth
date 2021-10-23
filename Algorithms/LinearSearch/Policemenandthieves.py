def count_theives(N, K, arr):

    if len(arr) < K:
        thief_count = 0
        police_count = 0
        for i in range(len(arr)): 
            if arr[i] == "T":
                thief_count = thief_count+1
            else: 
                police_count = police_count+1
        
        if thief_count<police_count:
            return thief_count
        else:
            return police_count

    count=0
    for i in range(len(arr)):
        if arr[i]=='T' and 'P' in arr:

            if i-K>=0:
                front=arr[i-K:i]
            else:
                front=arr[0:i]

            if i+K+1<=len(arr):
                end=arr[i+1:i+K+1]
            else:
                end=arr[i+1:len(arr)]

            if 'P' in front:
                count=count+1
                if i-K>=0:
                    front_index = (i-K)+front.index('P')
                else:
                    front_index = front.index('P')
                arr[front_index]="N"
            elif 'P' in end:
                count=count+1
                end_index = i+1+end.index('P')
                arr[end_index]="N"

    return count


tc = int(input())

for _ in range(tc):
    N, K = map(int, input().split())
    total=0
    for _ in range(N):
        arr = [ x for x in input().split() ]
        total = total+count_theives(N, K, arr)
    print(total)