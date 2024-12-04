import time
from day4_inputs import p1_sample, p1_puzzle

start_time = time.time()


def main():
    data_input = p1_puzzle
    data_array = data_input.strip().split("\n")
    full_data_array = []
    for entry in data_array:
        row_list = []
        for char in entry:
            row_list.append(char)
        full_data_array.append(row_list)
    xmas_search(array=full_data_array)


def xmas_search(array):
    xmas_count = 0
    for j, row in enumerate(array[:-1]):
        for i, char in enumerate(row[:-1]):
            first_x = False
            second_x = False
            if char == "A" and j > 0 and i > 0:
                if array[j - 1][i - 1] == "M":
                    if array[j + 1][i + 1] == "S":
                        first_x = True
                elif array[j - 1][i - 1] == "S":
                    if array[j + 1][i + 1] == "M":
                        first_x = True
                if array[j + 1][i - 1] == "M":
                    if array[j - 1][i + 1] == "S":
                        second_x = True
                elif array[j + 1][i - 1] == "S":
                    if array[j - 1][i + 1] == "M":
                        second_x = True
                if first_x and second_x:
                    xmas_count += 1
    print(xmas_count)


main()
print(time.time() - start_time)
