# DAY 3, QUESTION 1
import re
from collections import Counter


def massage_data(input):

    split_input = input.split(' ')
    coordinates = re.split(',|:', split_input[2])
    x_coord, y_coord = int(coordinates[0]), int(coordinates[1])
    area = split_input[3].split('x')
    width, height = int(area[0]), int(area[1])

    return x_coord, y_coord, width, height


def get_squares_of_fabric_within_two_claims():

    input_as_array = []

    with open('advent_of_code_3_input.txt', 'r') as input_file:
        for line in input_file:
            line_strip = line.strip('\n')
            input_as_array.append(line_strip)

    coordinates_and_area = list(map(massage_data, input_as_array))

    all_coordinates = []

    for x_coord, y_coord, width, height in coordinates_and_area:
        for current_horizontal_place in range(x_coord, x_coord + 1, width):
            for current_vertical_place in range(y_coord, y_coord + 1, height):
                all_coordinates.append(tuple((current_horizontal_place, current_vertical_place)))

    counter_of_all_coordinates = Counter(all_coordinates)

    overlapped_coordinates = 0

    for key, value in counter_of_all_coordinates:
        if value > 1:
            overlapped_coordinates += 1

    return overlapped_coordinates


# 1229 wrong answer, is too low
# 1230 wrong answer, is too low
# 661689 wrong answer, is too high
# FROM REDDIT: I think its better to Actually create a multidimentsional Array that is 1000x1000, then for each claim, loop through each Square of the claim and add +1 to that Square.

print(get_squares_of_fabric_within_two_claims())
