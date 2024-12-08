from functools import wraps


def restore_map_after(func):
    @wraps(func)
    def wrapper(lab_map, start_position, start_direction, *args, **kwargs):
        result = func(lab_map, start_position, start_direction, *args, **kwargs)

        # clean map
        explored_positions = result[0]
        for pos in explored_positions.keys():
            lab_map[pos[0]][pos[1]] = "."

        lab_map[start_position[0]][start_position[1]] = start_direction

        return result

    return wrapper


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


def find_guard_direction(lab_map, position):
    return lab_map[position[0]][position[1]]


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


@restore_map_after
def patrol(lab_map, start_position, start_direction, ending_condition="leave"):
    rows = len(lab_map)
    cols = len(lab_map[0])

    explored_positions = {start_position: [start_direction]}
    left_patrol = False

    x, y = start_position

    while not left_patrol:
        if lab_map[x][y] == "^":
            next_x, next_y = up(x, y)
            if lab_map[next_x][next_y] == "#":
                lab_map[x][y] = ">"
            else:
                x, y = up(x, y)
                lab_map[x][y] = "^"

        elif lab_map[x][y] == "v":
            next_x, next_y = down(x, y)
            if lab_map[next_x][next_y] == "#":
                lab_map[x][y] = "<"
            else:
                x, y = down(x, y)
                lab_map[x][y] = "v"

        elif lab_map[x][y] == "<":
            next_x, next_y = left(x, y)
            if lab_map[next_x][next_y] == "#":
                lab_map[x][y] = "^"
            else:
                x, y = left(x, y)
                lab_map[x][y] = "<"

        elif lab_map[x][y] == ">":
            next_x, next_y = right(x, y)
            if lab_map[next_x][next_y] == "#":
                lab_map[x][y] = "v"
            else:
                x, y = right(x, y)
                lab_map[x][y] = ">"

        left_patrol = is_leaving((x, y), lab_map[x][y], rows, cols)

        if ending_condition == "loop":
            if left_patrol == True:
                return (explored_positions, False)

            if lab_map[x][y] in explored_positions.get((x, y), []):
                return (explored_positions, True)

        if (x, y) not in explored_positions.keys():
            explored_positions[(x, y)] = [lab_map[x][y]]

    return (explored_positions, False)


def add_obstructions(lab_map, current_area, start_position, start_direction):
    total = 0
    for obstacle in current_area:
        lab_map[obstacle[0]][obstacle[1]] = "#"
        total += patrol(lab_map, start_position, start_direction, "loop")[1]
        lab_map[obstacle[0]][obstacle[1]] = "."
    return total


if __name__ == "__main__":
    lab_map = load_lab_map("Day_06/puzzle_input.txt")
    start_position = find_guard_position(lab_map)
    start_direction = find_guard_direction(lab_map, start_position)

    current_area = patrol(lab_map, start_position, start_direction)[0]
    del current_area[start_position]
    print(add_obstructions(lab_map, current_area, start_position, start_direction))
