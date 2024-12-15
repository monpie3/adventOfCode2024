DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def load_data(filename):
    with open(filename, "r") as f:
        map_data, moves = f.read().strip().split("\n\n")

    map_dict = {}
    for i, row in enumerate(map_data.split("\n")):
        for j, val in enumerate(row):
            map_dict[(i, j)] = val

    return map_dict, moves.replace("\n", "")


def find_robot_pos(warehouse_dic):
    for key, val in warehouse_dic.items():
        if val == "@":
            return key


def find_boxes_pos(warehouse_dic):
    boxes_pos = []
    for key, val in warehouse_dic.items():
        if val == "O":
            boxes_pos.append(key)
    return boxes_pos


def can_push_box(warehouse_dic, box_pos, direction):
    x, y = box_pos
    dx, dy = DIRECTIONS[direction]

    while warehouse_dic[x + dx, y + dy] != "#":
        if warehouse_dic[x + dx, y + dy] == ".":
            warehouse_dic[x + dx, y + dy] = "O"
            warehouse_dic[box_pos] = "@"
            return True

        x += dx
        y += dy

    return False


def move(warehouse_dic, current_pos, direction):
    x, y = current_pos
    dx, dy = DIRECTIONS[direction]

    new_pos = (x + dx, y + dy)
    if warehouse_dic[new_pos] == ".":
        warehouse_dic[current_pos] = "."
        warehouse_dic[new_pos] = "@"
        return new_pos

    if warehouse_dic[new_pos] == "#":
        return current_pos

    if warehouse_dic[new_pos] == "O":
        # check if there is space to move the box
        if can_push_box(warehouse_dic, new_pos, direction):
            warehouse_dic[current_pos] = "."  # if is, then clean earlier robot pos
            return new_pos

        else:
            return current_pos

    raise ValueError("Invalid move")


if "__main__" == __name__:
    warehouse_dic, robot_moves = load_data("Day_15/puzzle_input.txt")
    current_pos = find_robot_pos(warehouse_dic)
    for direction in robot_moves:
        current_pos = move(warehouse_dic, current_pos, direction)
    boxes_pos = find_boxes_pos(warehouse_dic)
    print(sum([box[0] * 100 + box[1] for box in boxes_pos]))
