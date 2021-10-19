n = int(input())
data = input()

if 'HH' in data: 
    print("NO")
else:
    print('YES')
    converted_data = data.replace('.', 'B')
    print(converted_data)