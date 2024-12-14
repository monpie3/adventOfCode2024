from task_13a import load_data, calculate_tokens
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_13/example_13a.txt", 480),
    ],
)
def test_calculate_tokens(file_path, expected):
    machines = load_data(file_path)
    assert calculate_tokens(machines) == expected