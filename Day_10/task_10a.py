def load_map(filename):
    with open(filename, "r") as f:
        map_data = f.read()

    return [[int(x) if x.isdigit() else x for x in row] for row in map_data.split()]


def is_within_bounds(point_x, point_y, max_row, max_col):
    return 0 <= point_x < max_row and 0 <= point_y < max_col


def count_score(
    point_x, point_y, target_val, achieved, topographic_map, max_row, max_col
):

    if target_val == 10:
        achieved.append((point_x, point_y))
        return 1

    score = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in directions:
        new_x, new_y = point_x + dx, point_y + dy
        if (
            is_within_bounds(new_x, new_y, max_row, max_col)
            and (new_x, new_y) not in achieved
            and topographic_map[new_x][new_y] == target_val
        ):

            score += count_score(
                new_x,
                new_y,
                target_val + 1,
                achieved,
                topographic_map,
                max_row,
                max_col,
            )
    return score


def find_trailhead(topographic_map):
    max_row = len(topographic_map)
    max_col = len(topographic_map[0])

    start_points = [
        (i, j)
        for i in range(max_row)
        for j in range(max_col)
        if topographic_map[i][j] == 0
    ]

    total_score = 0
    for start_x, start_y in start_points:
        achieved = []
        total_score += count_score(
            start_x,
            start_y,
            1,
            achieved,
            topographic_map,
            max_row,
            max_col,
        )

    return total_score


if "__main__" == __name__:
    topographic_map = load_map("Day_10/puzzle_input.txt")
    print(find_trailhead(topographic_map))
