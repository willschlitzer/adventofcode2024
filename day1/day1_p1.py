import time
from day1_inputs import p1_sample, p1_puzzle
start_time = time.time()

def main():
    left_list = []
    right_list = []
    entry_difference = 0

    input_split_rows = p1_puzzle.strip().split("\n")

    for row in input_split_rows:
        left, right = row_splitter(row)
        left_list.append(left)
        right_list.append(right)

        left_list.sort()
        right_list.sort()

    for i in range(len(left_list)):
        diff = abs(left_list[i] - right_list[i])
        entry_difference += diff
    end_time = time.time() - start_time
    print(entry_difference)
    print(end_time)


def row_splitter(row):
    left = int(row.split()[0])
    right = int(row.split()[1])
    return left, right


main()
