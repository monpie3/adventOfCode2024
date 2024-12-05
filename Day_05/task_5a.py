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


if __name__ == "__main__":
    rules, page_to_print = load_data("Day_05/puzzle_input.txt")
    page_to_print = [
        list(map(int, line.split(","))) for line in page_to_print.split("\n")
    ]
    rules_dict = proccess_rules(rules)

    valid_orders = []
    for order in page_to_print:
        if is_order_valid(order, rules_dict):
            valid_orders.append(order)

    middle_pages = [order[int(len(order) / 2)] for order in valid_orders]
    total = sum(middle_pages)
    print(f"{total=}")
