import math

def find_hex_decimal(num1, num2):
    count=0
    for i in range (num1, num2):
        total=0
        for each in hex(i).lstrip("0x"):
            total=total+int(each,16)
        if(math.gcd(i,total)>1):
            count=count+1
    return count

tc = int(input())
for _ in range(tc):
    L, R = map(int, input().split())
    print(find_hex_decimal(L, R+1))