def load_data(filename):
    with open(filename, "r") as f:
        data = f.read()

    return data.strip().split("\n\n")


def proccess_rules(rules):
    rules = rules.split("\n")

    rules_dict = {}
    for rule in rules:
        first_page, second_page = rule.split("|")

        first_page = int(first_page)
        second_page = int(second_page)

        if first_page not in rules_dict:
            rules_dict[first_page] = [second_page]
        else:
            rules_dict[first_page].append(second_page)
    return rules_dict


def is_order_valid(order, rules):
    # going through pages
    for index, page in enumerate(order):
        if page in rules:
            # going trough rules for page
            for second_page in rules[page]:
                # if page that should be second is before our page return False
                if second_page in order[:index]:
                    return False
    return True


def fix_orders(orders, rules):
    fixed_orders = []
    for order in orders:
        was_swapped = False
        # changing the order could break the rules
        # so if sth was swapped we need to check again
        while not was_swapped:
            was_swapped = True
            for index, page in enumerate(order):
                if page in rules:
                    # going trough rules for page
                    for second_page in rules[page]:
                        if second_page in order[:index]:
                            order[index], order[order.index(second_page)] = (
                                order[order.index(second_page)],
                                order[index],
                            )
                            was_swapped = False
        fixed_orders.append(order)
    return fixed_orders


if __name__ == "__main__":
    rules, page_to_print = load_data("Day_05/puzzle_input.txt")
    page_to_print = [
        list(map(int, line.split(","))) for line in page_to_print.split("\n")
    ]
    rules_dict = proccess_rules(rules)

    unvalid_orders = []
    for order in page_to_print:
        if not is_order_valid(order, rules_dict):
            unvalid_orders.append(order)

    fixed_orders = fix_orders(unvalid_orders, rules_dict)
    middle_pages = [order[int(len(order) / 2)] for order in fixed_orders]
    total = sum(middle_pages)
    print(f"{total=}")
