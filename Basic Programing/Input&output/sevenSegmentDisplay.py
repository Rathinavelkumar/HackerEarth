tc = int(input())
ms_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for each in range(tc):
    number = str(input())
    sum=0
    for each in number:
        sum  = sum + ms_list[int(each)]
        
    if sum%2==0:
        print('1'*int(sum//2))
    else:
        print('7' + '1'*(int(sum//2)-1))