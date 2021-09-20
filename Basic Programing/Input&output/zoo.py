input_word = str(input())

z_count = 0 
o_count = 0

for each_char in input_word:
    if each_char == 'z':
        z_count = z_count + 1
    elif each_char == 'o':
        o_count = o_count + 1

if z_count*2==o_count:
    print("Yes")
else:
    print("No")