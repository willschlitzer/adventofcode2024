from day2_inputs import p1_sample, p1_puzzle


def main():
    safe_count = 0
    rows_split = p1_sample.strip().split("\n")
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


def row_difference_check(row, row_increasing, bad_level_removed=False):
    if row_increasing:
        for i in range(len(row) - 1):
            bigger_value = row[i + 1]
            smaller_value = row[i]
            if not difference_checker(
                bigger_value=bigger_value, smaller_value=smaller_value
            ):
                if bad_level_removed:
                    return False
                else:
                    return deleted_item_checker(row=row, row_increasing=row_increasing)
        return True
    else:
        for i in range(len(row) - 1):
            bigger_value = row[i]
            smaller_value = row[i + 1]
            if not difference_checker(
                bigger_value=bigger_value, smaller_value=smaller_value
            ):
                if bad_level_removed:
                    return False
                else:
                    return deleted_item_checker(row=row, row_increasing=row_increasing)
        return True


def difference_checker(bigger_value, smaller_value):
    upper_diff = 3
    lower_diff = 1
    if (bigger_value - smaller_value < 1) or (bigger_value - smaller_value > 3):
        return False
    return True


def deleted_item_checker(row, row_increasing):
    for i in range(len(row)):
        temp_row = row.copy()
        del temp_row[i]
        if row_difference_check(
            row=temp_row, row_increasing=row_increasing, bad_level_removed=True
        ):
            return True
    return False


main()
