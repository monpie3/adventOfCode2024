from task_21a import load_data, find_shortest_path


def test_find_shortest_path():
    data = load_data("Day_21/example_21a.txt")
    complexity = []
    for code in data:
        complexity.append((len(find_shortest_path(code)), int(code[:-1])))
    assert complexity == [(68, 29), (60, 980), (68, 179), (64, 456), (64, 379)]
