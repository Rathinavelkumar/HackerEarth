tc = int(input())

for _ in range(tc):
    input_data = str(input())

    count=0
    for i in range(len(input_data)):
        if input_data[i]=='a' and (i+1)%4==1:
            count=count+1

    print(count)