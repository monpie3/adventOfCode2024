import pytest
from task_8b import load_map, find_antinodes


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_08/example_8a.txt", 34),
        ("Day_08/example_8b.txt", 9),
    ],
)
def test_find_antinodes(file_path, expected):
    map_data = load_map(file_path)
    result = find_antinodes(map_data)
    assert len(result) == expected
