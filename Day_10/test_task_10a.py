from task_10a import load_map, find_trailhead
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_10/example_10a.txt", 2),
        ("Day_10/example_10b.txt", 4),
        ("Day_10/example_10c.txt", 3),
        ("Day_10/example_10d.txt", 36),
    ],
)
def test_unpack_disk(file_path, expected):
    topographic_map = load_map(file_path)
    assert find_trailhead(topographic_map) == expected
