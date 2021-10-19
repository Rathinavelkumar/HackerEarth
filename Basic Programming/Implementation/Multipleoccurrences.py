tc = int(input())

for _ in range(tc):
    n = int(input())
    input_arr = list(map(int, input().split()))

    input_dict={}
    for i in range(n):
        if input_arr[i] in input_dict.keys():
            input_dict[input_arr[i]][0] = i
        else:
            input_dict[input_arr[i]] = [i,i]

    sum=0
    for each in input_dict:
        sum = sum + (input_dict[each][0]-input_dict[each][1])
    print(sum)