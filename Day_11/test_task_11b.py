from task_11b import blink
import pytest


@pytest.mark.parametrize(
    "test_input, blink_num, expected",
    [
        (
            [0, 1, 10, 99, 999],
            1,
            7,
        ),
        ([125, 17], 1, 3),
        ([125, 17], 2, 4),
        ([125, 17], 3, 5),
        ([125, 17], 4, 9),
        ([125, 17], 5, 13),
        ([125, 17], 6, 22),
    ],
)
def test_blink(test_input, blink_num, expected):
    assert blink(test_input, blink_num) == expected
