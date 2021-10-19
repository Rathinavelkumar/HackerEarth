size = int(input())
arr = list(map(int,input().split()))
start_index = 1
distance = 2

while start_index<=size:
    start_index = start_index + distance
    distance=distance+1
 
start_index = start_index-(distance-1)
distance=distance-2
total = sum(arr[:start_index])
temp_total = total
 
for i in range(1,size):
    total = total - arr[i-1]
    if start_index<size:
        total = total + arr[start_index]
        start_index = start_index + 1
    else:
        distance = distance - 1
        total = total - sum(arr[size-distance:size])
        start_index = start_index - distance
    if total > temp_total:
        temp_total = total
print(temp_total)