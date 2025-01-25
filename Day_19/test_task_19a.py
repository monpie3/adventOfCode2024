from task_19a import load_data, count_valid_designs
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_19/example_19a.txt", 6),
        pytest.param("Day_19/example_19b.txt", 1, id="greedy forward fails"),
        pytest.param("Day_19/example_19c.txt", 1, id="greedy backward fails"),
    ],
)
def test_find_trailhead(file_path, expected):
    towels, designs = load_data(file_path)
    valid = count_valid_designs(towels, designs)
    assert valid == expected
