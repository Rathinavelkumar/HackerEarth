N, A, B = map(int, input().split())

min_cost=[]
for i in range(0, N+1):
    cost = A*(i**2) + B*((N-i)**2)
    min_cost.append(cost)

print(min(min_cost))