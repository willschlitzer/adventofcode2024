import time
from day5_inputs import p1_sample_rules, p1_sample_lists, p1_puzzle_rules, p1_puzzle_lists

start_time = time.time()


def main():
    rules = p1_puzzle_rules
    updates = p1_puzzle_lists
    rules_list = get_rules_list(rules=rules)
    update_list = get_update_list(updates=updates)
    good_updates = []
    for update in update_list:
        order_fixed, update_new = check_page_fix(update=update, rule_list=rules_list)
        if order_fixed:
            good_updates.append(update_new)
    middle_num_sum = 0
    for good_update in good_updates:
        middle_index = int(len(good_update)/2)
        middle_value = good_update[middle_index]
        middle_num_sum += middle_value

    print(middle_num_sum)


def get_rules_list(rules):
    rules_list = []
    for rule in rules.strip().split("\n"):
        temp_rule = rule.split("|")
        temp_rule_list = []
        for rule_str in temp_rule:
            temp_rule_list.append(int(rule_str))
        rules_list.append(temp_rule_list)
    return rules_list

def get_update_list(updates):
    update_list = []
    for update in updates.strip().split("\n"):
        temp_update = update.split(",")
        temp_update_list = []
        for update_str in temp_update:
            temp_update_list.append(int(update_str))
        update_list.append(temp_update_list)
    return update_list

def check_page_fix(rule_list, update):
    order_fixed = False
    for rule in rule_list:
        x = rule[0]
        y = rule[1]
        for iy,ychar in enumerate(update):
            if ychar == y:
                for ix,xchar in enumerate(update):
                    if xchar == x:
                        if iy < ix:
                            update[ix] = ychar
                            update[iy] = xchar
                            order_fixed = True
    if order_fixed:
        if check_page(rule_list=rule_list, update=update):
            return True, update
        else: 
            return check_page_fix(rule_list=rule_list, update=update)
    else:
        return False, update


def check_page(rule_list, update):
    for rule in rule_list:
        x = rule[0]
        y = rule[1]
        for iy,ychar in enumerate(update):
            if ychar == y:
                for ix,xchar in enumerate(update):
                    if xchar == x:
                        if iy < ix:
                            return False
    return True


main()
print(time.time() - start_time)
