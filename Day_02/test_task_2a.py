from task_2a import is_save

import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_is_game_valid(test_input, expected):
    assert is_save(test_input) == expected
