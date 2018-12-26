# # DAY 1, QUESTION 2

def find_double_frequency():
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

    sum = 0
    all_sums = []

    duplicate_frequency = 0

    while duplicate_frequency == 0:
        for i in input_as_array:
            sum = sum + i
            if sum in all_sums:
                duplicate_frequency = sum
                break
            else:
                all_sums.append(sum)

    return duplicate_frequency


print(find_double_frequency()) # 245
