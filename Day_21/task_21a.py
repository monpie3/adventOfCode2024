NUMERIC_KEYPAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "None": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}

DIRECTIONAL_KEYPAD = {
    "None": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def load_data(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def sanitize_path(move, start, KEYPAD):
    x, y = start

    excluded = KEYPAD["None"]
    for m in move:
        if m == "^":
            x -= 1
        elif m == "v":
            x += 1
        elif m == "<":
            y -= 1
        elif m == ">":
            y += 1

        if (x, y) == excluded:
            return None
    return move


def min_cost(seq, depth):
    if depth == 0:
        return len(seq)
    sub_sequences = find_sequence(seq, directional=True, depth=depth)
    cost = min_cost(sub_sequences, depth - 1)
    return cost


def find_sequence(code, directional=False, depth=1):
    if directional:
        KEYPAD = DIRECTIONAL_KEYPAD
    else:
        KEYPAD = NUMERIC_KEYPAD

    start = KEYPAD["A"]
    sequence = []
    for key in code:
        move = ""
        end = KEYPAD[key]

        up = start[0] - end[0]
        left = start[1] - end[1]

        ver = "<" if left > 0 else ">"
        hor = "^" if up > 0 else "v"

        move_v = hor * abs(up) + ver * abs(left) + "A"
        move_h = ver * abs(left) + hor * abs(up) + "A"
        if move_h == move_v:
            move = move_h
        else:
            # check if not forbidden move
            sanitized_v = sanitize_path(move_v, start, KEYPAD)
            sanitized_h = sanitize_path(move_h, start, KEYPAD)
            move = sanitized_v or sanitized_h
            if sanitized_v and sanitized_h:
                # we have to check both
                cost_v = min_cost(sanitized_v, depth - 1)
                cost_h = min_cost(sanitized_h, depth - 1)
                move = sanitized_v if cost_v < cost_h else sanitized_h

        sequence.append(move)

        start = KEYPAD[key]
    return "".join(sequence)


def find_shortest_path(code):
    num_seq = find_sequence(code, depth=3)
    dir_seq = find_sequence(num_seq, directional=True, depth=2)
    dir_seq_2 = find_sequence(dir_seq, directional=True, depth=1)
    return dir_seq_2


if "__main__" == __name__:
    data = load_data("Day_21/puzzle_input.txt")
    complexity = []
    for code in data:
        complexity.append((len(find_shortest_path(code)), int(code[:-1])))
    print(complexity)

    total = 0
    for c in complexity:
        total += c[1] * c[0]
    print(total)
