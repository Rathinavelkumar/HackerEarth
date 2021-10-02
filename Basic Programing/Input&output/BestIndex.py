n = int(input())
data = [int(x) for x in input().split()]

sum_list = []
result = 0
for i in range(0,n):
    counter=1
    total = 0
    start_index = i
    end_index = i + counter

    while end_index<=n:
        print(data[start_index:end_index])
        total = total + sum(data[start_index:end_index])
        counter = counter + 1
        start_index = end_index
        end_index = end_index + counter

    if total>result:
        result=total

print(result)