input_data = input()

result=[]
for each in input_data:
    if each.isupper():
        result.append(each.lower())
    else:
        result.append(each.upper())

result = "".join(result)
print(result)