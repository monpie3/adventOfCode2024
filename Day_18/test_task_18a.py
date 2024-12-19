from task_18a import load_data, simulate_memory_failure, bfs


def test_simulate_memory_failure():
    width = 7
    height = 7
    grid = [["." for _ in range(width)] for _ in range(height)]

    byte_positions = load_data("Day_18/example_18a.txt")
    grid = simulate_memory_failure(grid, byte_positions, 12)
    path = bfs(grid, (0, 0), (height - 1, width - 1))
    assert len(path) - 1 == 22
