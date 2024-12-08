import itertools


def load_equations(filename):
    equations = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result, operands = line.strip().split(": ")
            equations.append((int(result), list(map(int, operands.split(" ")))))
    return equations


def is_calibration_possible(equation):
    result, operands = equation
    possible_orders = itertools.product(["*", "+", "||"], repeat=len(operands) - 1)

    for order in possible_orders:
        total = operands[0]
        for ind, operator in enumerate(order):
            if operator == "*":
                total *= operands[ind + 1]
            elif operator == "+":
                total += operands[ind + 1]
            elif operator == "||":
                total = int(str(total) + str(operands[ind + 1]))
            else:
                print("Unknown operator")
        if total == result:
            return True
    return False


if "__main__" == __name__:
    equations = load_equations("Day_07/puzzle_input.txt")
    valid_calibrations = 0
    for equation in equations:
        if is_calibration_possible(equation):
            valid_calibrations += equation[0]

    print(valid_calibrations)
