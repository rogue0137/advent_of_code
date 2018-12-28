# DAY 4, QUESTION 1
from collections import Counter

def put_file_into_array(file):
    array_of_info = []

    with open(file, 'r') as input_file:
        for line in input_file:
            strip_line = line.strip('\n')
            array_of_info.append(strip_line)

    return array_of_info


def split_each_array_into_two(info):

    split_line = info.split(' ')
    time = ' '.join(split_line[0:2])
    guard_specifics = ' '.join(split_line[2:])

    return [time, guard_specifics]


def choose_guard_and_time(file):

    array_of_info = put_file_into_array(file)

    sorted_array_of_info = sorted(array_of_info)

    info_broken_down = list(map(split_each_array_into_two, sorted_array_of_info))


    dict_of_guards = {}

    for index, one_entry in enumerate(info_broken_down):
        timestamp = one_entry[0]
        action = one_entry[1].split(' ')
        if action[0] == 'wakes':
            # get sleeping time
            sleep_info = info_broken_down[index - 1][0].split(' ')
            sleep_minute = int(sleep_info[1].replace(':','').replace(']',''))

            # get waking time
            wake_info = info_broken_down[index][0].split(' ')
            wake_minute = int(wake_info[1].replace(':','').replace(']',''))

            # get_guard_number
            guard_info = info_broken_down[index - 2][1].split(' ')
            guard_number = guard_info[1].replace('#','')

            for minute in range(sleep_minute, wake_minute):
                dict_of_guards.setdefault(guard_number, []).append(minute)

    counter_of_guards = {}

    for guard in dict_of_guards:
        counter_of_guards[guard] = len(dict_of_guards[guard])


    print(counter_of_guards)



print(choose_guard_and_time('advent_of_code_4_input.txt'))

# info_broken_down = [['[1518-02-22 23:58]', 'Guard #2543 begins shift'], ['[1518-02-23 00:15]', 'falls asleep'], ['[1518-02-23 00:41]', 'wakes up'], ['[1518-02-23 23:58]'
#    ...: , 'Guard #3571 begins shift'], ['[1518-02-24 00:20]', 'falls asleep'], ['[1518-02-24 00:59]', 'wakes up'], ['[1518-02-25 00:01]', 'Guard #1697 begins shift'], ['[1518-02
#    ...: -25 00:08]', 'falls asleep'], ['[1518-02-25 00:35]', 'wakes up']]
