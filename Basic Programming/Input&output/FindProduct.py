n = int(input())
data = [ int(x) for x in input().split() ]

result=1
for each in data:
    result = (result * each) % (1000000000+7)

print(result)