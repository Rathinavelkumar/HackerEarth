tc = int(input())

count=0
for _ in range(tc):
    length, breath = map(int, input().split())
    if (length/breath>=1.6 and length/breath<=1.7) or (breath/length>=1.6 and breath/length<=1.7):
        count=count+1

print(count)