testcases_count = int(input())

for testcase in range(0, testcases_count):
    dimension = input()
    row, column = dimension.split()

    border_list=[]
    first = 0
    last = 0

    for each_row in range(0, int(row)):
        data = input()
        row_length = data.count("#")
        current_index = data.find("#")
        end_index = current_index+row_length-1

        if first==0 and last==0 : length=end_index-current_index+1
        elif current_index<first and end_index<first: length=end_index-current_index+1
        elif current_index>first and end_index<last: length=0
        elif current_index==first and end_index>last: length=end_index-last
        elif current_index>last: length=end_index-current_index+1

        border_list.append(length)
        first = current_index
        last = end_index

    print(max(border_list))