def calculate_factorial(num):
    if num==1:
        return 1
    else:
        return num * calculate_factorial(num-1)

input_data = int(input())
print(calculate_factorial(input_data))