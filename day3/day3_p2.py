import time
from day3_inputs import p2_sample, p1_puzzle
import re
start_time = time.time()


def main():
    data_input = p1_puzzle
  #  data_input = p2_sample
    dont_split = data_input.split("don't()")
    math_string = dont_split[0]
    do_list = [math_string]
    for x in dont_split[1:]:
        y = x.split("do()")
        do_list.append(y[1])
        print(do_list)
    
    final_string = "".join(do_list)
    find_multis(data_input=final_string)

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
#print(time.time() - start_time)