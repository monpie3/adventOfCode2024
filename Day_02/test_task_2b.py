from task_2b import problem_dampener

import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_problem_dampener(test_input, expected):
    assert problem_dampener(test_input) == expected
