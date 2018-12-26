# # DAY 2, QUESTION 1
from collections import Counter

def get_checksum():
  with open('advent_of_code_2_input.txt', 'r') as input_file:

    count_of_letters = {'two': 0, 'three': 0}

    for line in input_file:
        line_counter = Counter(line)
        switched_counter = {count:letter for letter,count in line_counter.items()}
        if 2 in switched_counter:
            count_of_letters['two'] = count_of_letters['two'] + 1
        if 3 in switched_counter:
            count_of_letters['three'] = count_of_letters['three'] + 1



    checksum = count_of_letters['two'] * count_of_letters['three']

    return checksum

print(get_checksum()) # 5750
