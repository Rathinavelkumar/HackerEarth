input_string = input()

vowels = list('AEIOUY')

Val_1, Val_2 = int(input_string[0]), int(input_string[1])
Val_3, Val_4, Val_5 = int(input_string[3]), int(input_string[4]), int(input_string[5])
Val_6, Val_7 = int(input_string[7]), int(input_string[8])

if input_string[2] in vowels:
    print('invalid')
elif (Val_1+Val_2)%2!=0 or (Val_4+Val_4)%2!=0 or (Val_4+Val_5)%2!=0 or (Val_6+Val_7)%2!=0:
    print('invalid')
else:
    print('valid')