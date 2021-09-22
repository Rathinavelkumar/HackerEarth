array_size = int(input())
elements = input()

filtered_list1 = [ x[0] for i, x in enumerate(elements.split(" ")) if i < array_size/2]
filtered_list2 = [ x[-1] for i, x in enumerate(elements.split(" ")) if i >= array_size/2]
result = ''.join(filtered_list1) + ''.join(filtered_list2)

if int(result)%11==0:
    print("OUI")
else:
    print("NON")