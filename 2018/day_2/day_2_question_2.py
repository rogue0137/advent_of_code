# DAY 2, QUESTION 2
import itertools
from difflib import SequenceMatcher

def get_santas_boxes():
    input_as_array = []

    with open('advent_of_code_2_input.txt', 'r') as input_file:
        for line in input_file:
            line_strip = line.strip('\n')
            input_as_array.append(line_strip)

    for first_box, second_box in itertools.combinations(input_as_array, 2):
        seq = SequenceMatcher(None, first_box, second_box)
        r = seq.ratio()

        if r == 0.9615384615384616:
            similar_chars = ''

            for box_1_char, box_2_char in zip(first_box, second_box):
                if box_1_char == box_2_char:
                    similar_chars += box_1_char

            return similar_chars



print(get_santas_boxes()) # tzyvunogzariwkpcbdewmjhxi


# IF TIME PERMITS: Go back and do this in code
# 0.9615384615384616c comes from changing a list of 26 characters by 1 character; first list ends in 'i', second list ends in 'q'
# >>> from difflib import SequenceMatcher
# >>> list1 = ''.join(['t', 'q', 'z', 'v', 'w', 'n', 'o', 'g', 'b', 'a', 'r', 'f', 'l', 'k', 'p', 'c', 'b', 'd', 'e', 'w', 's', 'm', 'j', 'h', 'x', 'i'])
# >>> list1
# 'tqzvwnogbarflkpcbdewsmjhxi'
# >>> list2 = ''.join(['t', 'q', 'z', 'v', 'w', 'n', 'o', 'g', 'b', 'a', 'r', 'f', 'l', 'k', 'p', 'c', 'b', 'd', 'e', 'w', 's', 'm', 'j', 'h', 'x', 'q'])
# >>> seq = SequenceMatcher(None, list1, list2)
# >>> seq
# <difflib.SequenceMatcher object at 0x106e21518>
# >>> seq.ratio()
# 0.9615384615384616
