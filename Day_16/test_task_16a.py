from task_16a import load_map, find_best_score
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_16/example_16a.txt", 7036),
        ("Day_16/example_16b.txt", 11048),
    ],
)
def test_find_best_score(file_path, expected):
    tiles = load_map(file_path)
    assert find_best_score(tiles) == expected
