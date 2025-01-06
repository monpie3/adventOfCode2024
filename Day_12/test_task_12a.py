from task_12a import load_garden_data, calculate_price
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_12/example_12a.txt", 140),
        ("Day_12/example_12b.txt", 772),
        ("Day_12/example_12c.txt", 1930),
    ],
)
def test_calculate_price(file_path, expected):
    garden = load_garden_data(file_path)
    assert calculate_price(garden) == expected
