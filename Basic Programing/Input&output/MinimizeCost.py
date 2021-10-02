from typing import Text


size, k = map(int,input().split(" "))
input_array = [int(each) for each in input().split()]
transpose_array = [0 for _ in range(0,size)]

final_list=[]
for i in range(size):
    diff = transpose_array[i]-input_array[i]
    if diff<=k:
        transpose_array[i] = diff

    final_list.append(abs(input_array[i]+transpose_array[i]))

print(input_array)
print(transpose_array)
print(final_list)
print(sum(final_list))