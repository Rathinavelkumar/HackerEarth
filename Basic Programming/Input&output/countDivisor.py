input_num = input()

l, r, k =  input_num.split(" ")

count=0
for i in range(int(l), int(r)+1):
    if i%int(k)==0:
        count = count +1

print(count)