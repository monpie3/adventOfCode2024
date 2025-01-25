from task_19b import load_data, count_ways
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_19/example_19a.txt", 16),
    ],
)
def test_find_trailhead(file_path, expected):
    towels, designs = load_data(file_path)
    valid = count_ways(towels, designs)
    assert valid == expected
