import collections


def load_map(filename):
    with open(filename, "r") as f:
        map_data = f.read()

    return [list(row) for row in map_data.split()]


def bfs(grid, start, end):
    height = len(grid)
    width = len(grid[0])
    end_x, end_y = end
    queue = collections.deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == end_x and y == end_y:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < height
                and 0 <= ny < width
                and grid[nx][ny] != "#"
                and (nx, ny) not in visited
            ):
                queue.append(path + [(nx, ny)])
                visited.add((nx, ny))
    return path


def find_pos(grid, el):
    for row_ind, row in enumerate(grid):
        for col_ind, cell in enumerate(row):
            if cell == el:
                return (row_ind, col_ind)


def is_within_bounds(point_x, point_y, max_row, max_col):
    return 0 <= point_x < max_row and 0 <= point_y < max_col


def find_cheat_positions(racepath, field, max_row, max_col, threshold):
    start_ind = racepath.index(field)
    x, y = field

    pos = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx1, dy1 in directions:
        nx1, ny1 = x + dx1, y + dy1
        if is_within_bounds(nx1, ny1, max_row, max_col):
            for dx2, dy2 in directions:
                nx2, ny2 = nx1 + dx2, ny1 + dy2
                # check if is back on normal track again
                if (
                    is_within_bounds(nx2, ny2, max_row, max_col)
                    and (nx2, ny2) in racepath
                ):
                    end_ind = racepath.index((nx2, ny2))
                    if start_ind - end_ind - 2 >= threshold:
                        # we need to spend 2 picoseconds for the cheating
                        pos.add(((x, y), (nx2, ny2)))
    return pos


def cheat_threshold(racetrack, threshold):
    start = find_pos(racetrack, "S")
    end = find_pos(racetrack, "E")
    racepath = bfs(
        racetrack, start, end
    )  # there is only a single path from the start to the end
    max_row = len(racetrack)
    max_col = len(racetrack[0])

    pos = set()
    for field in racepath:
        pos.update(find_cheat_positions(racepath, field, max_row, max_col, threshold))

    return pos


if "__main__" == __name__:
    racetrack = load_map("Day_20/puzzle_input.txt")
    pos = cheat_threshold(racetrack, 100)
    print(len(pos))
