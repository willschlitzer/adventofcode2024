from day1_inputs import p1_sample, p1_puzzle


def main():
    left_list = []
    right_list = []
    similarity_score = 0

    input_split_rows = p1_puzzle.strip().split("\n")

    for row in input_split_rows:
        left, right = row_splitter(row)
        left_list.append(left)
        right_list.append(right)

    for value in left_list:
        value_count = right_list.count(value)
        similarity_score += value * value_count

    print(similarity_score)


def row_splitter(row):
    left = int(row.split()[0])
    right = int(row.split()[1])
    return left, right


main()
