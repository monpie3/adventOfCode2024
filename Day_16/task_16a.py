import heapq


def load_map(filename):
    with open(filename) as f:
        return f.read().splitlines()


def find_tile(tiles, tile_name):
    for i, line in enumerate(tiles):
        if tile_name in line:
            return (i, line.index(tile_name))


def dijkstra_alg(grid, start, width, height):
    wall, goal = "#", "E"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    direction_names = ["^", "v", "<", ">"]

    # Priority queue (cost, position, last direction, path)
    start_x, start_y = start
    pq = []
    visited = set()

    heapq.heappush(pq, (0, start_x, start_y, ">", []))

    while pq:
        cost, x, y, last_dir, path = heapq.heappop(pq)

        # If we reached the goal
        if grid[x][y] == goal:
            print("Final cost:", cost)
            return cost

        # Avoid revisiting the same position with the same last direction
        if (x, y, last_dir) in visited:
            continue
        visited.add((x, y, last_dir))

        # Add neighbors to the queue
        for (dx, dy), dir_name in zip(directions, direction_names):
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < height
                and 0 <= new_y < width
                and grid[new_x][new_y] != wall
            ):
                # Calculate the movement cost
                new_cost = cost + 1

                # Add penalty for changing direction
                if last_dir != dir_name:
                    new_cost += 1000

                heapq.heappush(pq, (new_cost, new_x, new_y, dir_name, path + [(x, y)]))


def find_best_score(tiles):
    width = len(tiles[0])
    height = len(tiles)
    start = find_tile(tiles, "S")
    return dijkstra_alg(tiles, start, width, height)


if __name__ == "__main__":
    tiles = load_map("Day_16/puzzle_input.txt")
    score = find_best_score(tiles)
    print("Score:", score)
