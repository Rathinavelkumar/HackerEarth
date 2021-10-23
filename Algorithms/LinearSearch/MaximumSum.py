n = int(input())

arr = list(map(int, input().split()))

count=0
sum=0
for each in arr:
    if each>=0:
        count=count+1
        sum = sum + each

if count>0:
    print(sum, count)
else:
    print(max(arr), 1)