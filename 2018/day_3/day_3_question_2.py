# DAY 3, QUESTION 2
import re
import numpy as np

def massage_data(input):

    split_input = input.split(' ')
    claim = int(split_input[0].replace('#', ''))
    coordinates = re.split(',|:', split_input[2])
    x_coord, y_coord = int(coordinates[0]), int(coordinates[1])
    area = split_input[3].split('x')
    width, height = int(area[0]), int(area[1])

    return claim, x_coord, y_coord, width, height


def get_nonoverlapping_claim():

    input_as_array = []

    with open('advent_of_code_3_input.txt', 'r') as input_file:
        for line in input_file:
            line_strip = line.strip('\n')
            input_as_array.append(line_strip)

    claim_coordinates_and_area = list(map(massage_data, input_as_array))

    # creates a matrix 1000 width by 1000 height
    fabric = np.zeros((1000, 1000))

    # this iterates through all claims and adds +1 where someone has
    # claimed that square of fabric
    # if more than one person has claimed that square, it will continue
    # to add 1
    for claim, x_coord, y_coord, width, height in claim_coordinates_and_area:
        fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1

    for claim, x_coord, y_coord, width, height in claim_coordinates_and_area:
        if np.all(fabric[x_coord: x_coord + width, y_coord: y_coord + height] == 1):
            return claim


print(get_nonoverlapping_claim()) # 243 --> # 243 @ 204,784: 11x27



# >>> import numpy as np
# >>> fabric = np.zeroes((5,5))
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 2., 0., 0., 0.],
#        [0., 2., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> fabric = np.zeros((5,5))
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> claim, x_coord, y_coord, width, height = 366, 1, 1, 2, 2
# >>> fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 1., 1., 0., 0.],
#        [0., 1., 1., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> fabric = np.zeros((5,5))
# >>> claim, x_coord, y_coord, width, height = 366, 1, 1, 1, 2
# >>> fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 1., 1., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
# >>> claim, x_coord, y_coord, height, width = 366, 1, 1, 1, 2
# >>> fabric = np.zeros((5,5))
# >>> fabric[x_coord: x_coord + width, y_coord: y_coord + height] += 1
# >>> fabric
# array([[0., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])
