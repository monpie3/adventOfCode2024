from task_18a import load_data, simulate_memory_failure, bfs


def test_simulate_memory_failure():
    width = 7
    height = 7
    grid = [["." for _ in range(width)] for _ in range(height)]
    byte_positions = load_data("Day_18/example_18a.txt")

    for byte in byte_positions:
        byte_y, byte_x = byte
        grid[byte_x][byte_y] = "#"
        path = bfs(grid, (0, 0), (height - 1, width - 1))

        if path == "No path found!":
            print(f"{byte_y},{byte_x}")
            break

    assert byte_y, byte_x == (6, 1)
