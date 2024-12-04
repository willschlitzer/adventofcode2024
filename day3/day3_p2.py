import time
from day3_inputs import p2_sample, p1_puzzle
import re

start_time = time.time()


def main():
    data_input = p1_puzzle
    # data_input = p2_sample
    find_pattern(input_string=data_input)
    dont_pattern = r"don\'t\(\)"
    dont_matches = re.findall(dont_pattern, data_input)
    for _ in range(len(dont_matches)):
        data_input = remove_dont_func(input_string=data_input)
    # print(data_input)
    dont_matches = re.findall(dont_pattern, data_input)
    # find_multis(data_input=data_input)
    find_pattern(input_string=data_input)


def find_pattern(input_string):
    do_pattern = r"(do\(\))(.+?)(don\'t\(\))"
    do_matches = re.findall(do_pattern, input_string)
    do_match_list = [x for x in do_matches]
    for i in do_match_list:
        print(i)


def remove_dont_func(input_string):
    remove_pattern = r"(don\'t\(\))(.+?)(do\(\)|$)"
    return re.sub(pattern=remove_pattern, repl="_", string=input_string)


def find_multis(data_input):
    total_count = 0
    pattern = r"mul\(\d+\,\d+\)"
    matches = re.findall(pattern=pattern, string=data_input)
    for match in matches:
        num_pattern = r"\d+\,\d+"
        num_match_str = re.findall(num_pattern, match)[0]
        multi_nums = [int(x) for x in num_match_str.split(",")]
        multi_total = multi_nums[0] * multi_nums[1]
        total_count += multi_total

    print(total_count)


main()
# print(time.time() - start_time)
