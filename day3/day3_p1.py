import time
from day3_inputs import p1_sample, p1_puzzle
import re
start_time = time.time()


def main():
    data_input = p1_puzzle
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
print(time.time() - start_time)
