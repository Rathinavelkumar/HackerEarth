def bi_search(arr,num):
    first_index=0
    last_index=len(arr)-1
    search_index=-1

    if num>arr[last_index]:
        return -1 
    elif num<arr[0]:
        return 0

    while (first_index<=last_index) and (search_index==-1):
        mid=(first_index+last_index)//2
        if arr[mid]==num or (num>arr[mid-1] and num<arr[mid]):
            search_index=mid
        elif arr[mid]<num:
            first_index=mid+1
        elif arr[mid]>num:
            last_index=mid-1

    return search_index

T = int(input())
total, res_arr = 0, []
for each in input().split():
    total=total+int(each)
    res_arr.append(total)

target=int(input())
for _ in range(target):
    num = int(input())
    result = bi_search(res_arr,num)
    print(result+1) if result>=0 else print(-1)