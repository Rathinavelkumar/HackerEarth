size = int(input())
data = input()

list_data = data.split(' ')
filter_data = [each[-1] for each in list_data]
result_data = ''.join(filter_data)

if int(result_data)%10==0:
    print('Yes')
else: 
    print('No')