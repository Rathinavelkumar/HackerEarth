n = int(input())

for _ in range(n):
    num = int(input())
    if num%21==0 or ('21' in str(num)):
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')