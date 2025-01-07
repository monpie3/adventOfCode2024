from task_12b import load_garden_data, calculate_price
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_12/example_12a.txt", 80),
        ("Day_12/example_12b.txt", 436),
        ("Day_12/example_12c.txt", 1206),
        ("Day_12/example_12d.txt", 236),
        ("Day_12/example_12e.txt", 368),
    ],
)
def test_calculate_price(file_path, expected):
    garden = load_garden_data(file_path)
    assert calculate_price(garden) == expected
