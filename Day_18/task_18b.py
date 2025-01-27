import collections


def load_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    return [list(map(int, row.split(","))) for row in data]


# https://stackoverflow.com/questions/47896461/get-shortest-path-to-a-cell-in-a-2d-array-in-python
def bfs(grid, start, end):
    height = len(grid)
    width = len(grid[0])
    end_x, end_y = end

    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == end_x and y == end_y:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= x2 < width
                and 0 <= y2 < height
                and grid[y2][x2] != "#"
                and (x2, y2) not in seen
            ):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return "No path found!"


if __name__ == "__main__":
    width = 71
    height = 71
    grid = [["." for _ in range(width)] for _ in range(height)]
    byte_positions = load_data("Day_18/puzzle_input.txt")

    for byte in byte_positions:
        byte_y, byte_x = byte
        grid[byte_x][byte_y] = "#"
        path = bfs(grid, (0, 0), (height - 1, width - 1))
        if path == "No path found!":
            print(f"{byte_y},{byte_x}")
            break
