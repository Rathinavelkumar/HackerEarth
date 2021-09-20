n = int(input())
data = input()

flag=False
if 'HH' in data: 
    print("NO")
else:
    print('YES')
    flag=True

if flag==True:
    converted_data = data.replace('.', 'B')
    print(converted_data)