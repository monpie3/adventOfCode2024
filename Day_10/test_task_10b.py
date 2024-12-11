from task_10b import load_map, find_trailhead_by_rating
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_10/example_10e.txt", 3),
        ("Day_10/example_10b.txt", 13),
        ("Day_10/example_10f.txt", 227),
        ("Day_10/example_10g.txt", 81),
    ],
)
def test_find_trailhead_by_rating(file_path, expected):
    topographic_map = load_map(file_path)
    assert find_trailhead_by_rating(topographic_map) == expected
