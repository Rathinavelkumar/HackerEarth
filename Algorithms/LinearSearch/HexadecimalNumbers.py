import math

def find_hex_decimal(num1, num2):
    count=0
    #Iterating each number between the given range
    for i in range(num1, num2):
        total=0
        #Get the hex value of given digit and remove the "0x"
        for each in hex(i).lstrip("0x"):
            #int(each,16) helps to covert a hex number to integer
            total=total+int(each,16)
        #Finally check the greatest common divisor
        #If, its greater than 1, increment the count
        if(math.gcd(i,total)>1):
            count=count+1
    return count

tc = int(input())
for _ in range(tc):
    L, R = map(int, input().split())
    print(find_hex_decimal(L,R+1))