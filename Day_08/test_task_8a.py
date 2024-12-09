from task_8a import load_map, find_antinodes


def test_find_antinodes():
    map_data = load_map("Day_08/example_8a.txt")
    assert len(find_antinodes(map_data)) == 14
