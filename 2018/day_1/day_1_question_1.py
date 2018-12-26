# DAY 1, QUESTION 1

with open('advent_of_code_1_input.txt', 'r') as input_file:

    input_as_array = []

    for line in input_file:
        line_as_array = list(line)
        if line_as_array[0] == '+':
            del line_as_array[0]
            new_int = int(''.join(line_as_array))
            input_as_array.append(new_int)
        else:
            new_int = int(line)
            input_as_array.append(new_int)

final_answer = sum(input_as_array)
print(final_answer # 435
