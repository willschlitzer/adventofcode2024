from day2_inputs import p1_sample, p1_puzzle


def main():
    safe_count = 0
    rows_split = p1_puzzle.strip().split("\n")
    for row in rows_split:
        int_row = [int(x) for x in row.split()]
        safety_value = row_safety(row=int_row)
        if safety_value:
            safe_count += 1
    print(safe_count)


def row_safety(row):
    if row[0] < row[-1]:
        return row_difference_check(row=row, row_increasing=True)
    elif row[0] > row[-1]:
        return row_difference_check(row=row, row_increasing=False)
    else:
        return False


def row_difference_check(row, row_increasing):
    if row_increasing:
        for i in range(len(row) - 1):
            if (row[i + 1] - row[i] < 1) or (row[i + 1] - row[i] > 3):
                return False
        return True
    else:
        for i in range(len(row) - 1):
            if (row[i] - row[i + 1] < 1) or (row[i] - row[i + 1] > 3):
                return False
        return True


main()
