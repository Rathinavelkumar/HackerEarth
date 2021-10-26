import bisect

T = int(input())
total, res_arr = 0, []
for each in input().split():
    total=total+int(each)
    res_arr.append(total)

target=int(input())
for _ in range(target):
    num = int(input())
    print(-1) if num>res_arr[len(res_arr)-1] else print(bisect.bisect_left(res_arr,num)+1)