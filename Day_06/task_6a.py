def load_lab_map(filename):
    lab_map = ""
    with open(filename, "r") as f:
        lab_map = f.read()

    return [list(row) for row in lab_map.split()]


def up(row, col):
    return row - 1, col


def right(row, col):
    return row, col + 1


def left(row, col):
    return row, col - 1


def down(row, col):
    return row + 1, col


def find_guard_position(lab_map):
    for index, row in enumerate(lab_map):
        if "^" in row:
            return index, row.index("^")
        if "v" in row:
            return index, row.index("v")
        if ">" in row:
            return index, row.index(">")
        if "<" in row:
            return index, row.index("<")


def is_leaving(cur_pos, direciton, rows, cols):
    cur_x, cur_y = cur_pos
    if direciton == "^" and cur_x == 0:
        return True
    if direciton == "v" and cur_x == rows - 1:
        return True
    if direciton == "<" and cur_y == 0:
        return True
    if direciton == ">" and cur_y == cols - 1:
        return True
    return False


def patrol(lab_map):
    rows = len(lab_map)
    cols = len(lab_map[0])

    start_position = find_guard_position(lab_map)
    explored_positions = {start_position}
    left_patrol = False

    x, y = start_position

    while not left_patrol:
        if lab_map[x][y] == "^":
            next_x, next_y = up(x, y)
            if lab_map[next_x][next_y] == "#":
                x, y = right(x, y)
                lab_map[x][y] = ">"
            else:
                x, y = up(x, y)
                lab_map[x][y] = "^"

        elif lab_map[x][y] == "v":
            next_x, next_y = down(x, y)
            if lab_map[next_x][next_y] == "#":
                x, y = left(x, y)
                lab_map[x][y] = "<"
            else:
                x, y = down(x, y)
                lab_map[x][y] = "v"

        elif lab_map[x][y] == "<":
            next_x, next_y = left(x, y)
            if lab_map[next_x][next_y] == "#":
                x, y = up(x, y)
                lab_map[x][y] = "^"
            else:
                x, y = left(x, y)
                lab_map[x][y] = "<"

        elif lab_map[x][y] == ">":
            next_x, next_y = right(x, y)
            if lab_map[next_x][next_y] == "#":
                x, y = down(x, y)
                lab_map[x][y] = "v"
            else:
                x, y = right(x, y)
                lab_map[x][y] = ">"

        explored_positions.add((x, y))
        left_patrol = is_leaving((x, y), lab_map[x][y], rows, cols)

    return explored_positions


if __name__ == "__main__":
    lab_map = load_lab_map("Day_06/puzzle_input.txt")
    print(len(patrol(lab_map)))
