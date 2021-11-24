km = int(input())

c, f, d = map(int, input().split())
online_cost = c + ((km-f)*d)

s, b, m, d = map(int, input().split())
classic_cost = b + ((km//s)*m) + (km*d)

print(online_cost, classic_cost)
if online_cost<=classic_cost:
    print('Online Taxi')
else:
    print('Classic Taxi')