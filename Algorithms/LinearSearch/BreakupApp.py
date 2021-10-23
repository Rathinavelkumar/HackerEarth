n = int(input())

result = {19:0,20:0}
for _ in range(n):
    message = input()

    datestr = list( int(x) for x in message.split() if x.isdigit() )
    weightage = 2 if message[:1] == 'G' else 1

    for each in datestr:
        if each in result.keys():
            result[each] = result[each] + weightage
        else:
            result[each]=weightage

final = [ int(k) for k,v in result.items() if v == max(result.values()) ]
if len(final)==1 and (final[0]==19 or final[0]==20):
    print('Date')
else:
    print('No Date')