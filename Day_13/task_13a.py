import re
from sympy import symbols, Eq, solve

A_PRICE = 3
B_PRICE = 1


def load_data(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n\n")

    machines = []
    for machine in data:
        machine = re.findall(r"\d+", machine)
        machine = list(map(int, machine))
        machines.append(machine)

    return machines


def find_way_to_win(machine):
    a1, a2, b1, b2, r1, r2 = machine

    x, y = symbols("x,y")
    eq1 = Eq((a1 * x + b1 * y), r1)
    eq2 = Eq((a2 * x + b2 * y), r2)

    sol_dict = solve((eq1, eq2), (x, y))
    x = sol_dict[x]
    y = sol_dict[y]

    if x == int(x) and y == int(y):
        return x, y
    else:
        return 0, 0


def calculate_tokens(machines):
    token = 0
    for machine in machines:
        a, b = find_way_to_win(machine)
        token += a * A_PRICE + b * B_PRICE
    return token


if "__main__" == __name__:
    machines = load_data("Day_13/puzzle_input.txt")
    print(calculate_tokens(machines))
