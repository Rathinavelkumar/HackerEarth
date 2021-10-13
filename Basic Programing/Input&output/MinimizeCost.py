size,k = map(int, input().split())
arr = map(int, input().split())

total=0
counter=0
m=k
flag=False

for i in arr:

    if flag==False:
            if(i>=0):
                counter=counter+1
                total=total+i
                m=k
            else:
                if(counter==0):
                    print(abs(sum(arr)+i))
                    flag=True
                else:
                    m-=1
                    if(m<0):
                        total=total+abs(i)
                    else:
                        total=total+i
    else:
        break

if flag==False:
    print(abs(total))