n = int(input())

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

min_val = min(first_array)
count=0

i=0
while i < n:
    while first_array[i]>min_val:
        first_array[i] = first_array[i] - second_array[i]
        count=count+1
    if first_array[i]<min_val:
        min_val=first_array[i]
        i=0
    elif first_array[i]<0:
        count=-1
        break
    else:
        i=i+1

print(count)