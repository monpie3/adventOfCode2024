from task_7b import is_calibration_possible
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((190, [10, 19]), True),
        ((3267, [81, 40, 27]), True),
        ((83, [17, 5]), False),
        ((156, [15, 6]), True),
        ((7290, [6, 8, 6, 15]), True),
        ((161011, [16, 10, 13]), False),
        ((192, [17, 8, 14]), True),
        ((21037, [9, 7, 18, 13]), False),
        ((292, [11, 6, 16, 20]), True),
    ],
)
def test_is_calibration_possible_extended(test_input, expected):
    assert is_calibration_possible(test_input) == expected
