tc = int(input())

for _ in range(tc):
    N, A, B = map(int, input().split())
    # (A*(X**2)) + (B*((N-X)**2))
    # differentiate the above quadratic equation to find minimum point
    X = N*B//(A+B)
    Y = N-X

    res1 = A*(X**2) + B*(Y**2)
    res2 = A*((X+1)**2) + B*((Y-1)**2)
    print(min(res1,res2))
