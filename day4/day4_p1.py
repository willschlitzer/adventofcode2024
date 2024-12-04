import time
from day4_inputs import p1_sample, p1_puzzle
import re
import numpy as np

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
    full_data_np = np.array(full_data_array)
    full_data_np_tp = np.transpose(full_data_np)
    search_words = ["XMAS", "SAMX"]
    xmas_count = 0
    for word in search_words:
        xmas_count += word_search(word=word, array=full_data_np)
        xmas_count += diagonal_word_search(word=word, array=full_data_np)

        xmas_count += word_search(word=word, array=full_data_np_tp)

    print(xmas_count)


def word_search(word, array):
    single_xmas_count = 0
    for row in array:
        for i, char in enumerate(row[:-3]):
            if char == word[0]:
                if row[i + 1] == word[1]:
                    if row[i + 2] == word[2]:
                        if row[i + 3] == word[3]:
                            single_xmas_count += 1
    return single_xmas_count


def diagonal_word_search(word, array):
    single_xmas_count = 0
    for j, row in enumerate(array[:-3]):
        for i, char in enumerate(row):
            if char == word[0]:
                if i >= 3:
                    if array[j + 1][i - 1] == word[1]:
                        if array[j + 2][i - 2] == word[2]:
                            if array[j + 3][i - 3] == word[3]:
                                print(array[j + 3][i - 3])
                                single_xmas_count += 1
                if i < len(row) - 3:
                    if array[j + 1][i + 1] == word[1]:
                        if array[j + 2][i + 2] == word[2]:
                            if array[j + 3][i + 3] == word[3]:
                                single_xmas_count += 1
    return single_xmas_count


main()
# print(time.time() - start_time)
