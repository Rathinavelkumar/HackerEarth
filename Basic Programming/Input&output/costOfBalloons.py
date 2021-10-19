testcase = int(input())

for tc in range(0,testcase):
    first, second = input().split(" ")
    if tc%2==0:
        first, second = int(first), int(second)
    else:
        second, first = int(first), int(second)
    participants = int(input())
    cost = 0
    for each_person in range(0, participants):
        value1, value2 = input().split(" ")
        cost = cost  + (int(value1) * first)
        cost = cost  + (int(value2) * second)
    print(cost)