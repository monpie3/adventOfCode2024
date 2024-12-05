from task_5a import load_data, proccess_rules, is_order_valid

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([75, 47, 61, 53, 29], True),
        ([97, 61, 53, 29, 13], True),
        ([75, 29, 13], True),
        ([75, 97, 47, 61, 53], False),
        ([61, 13, 29], False),
        ([97, 13, 75, 29, 47], False),
    ],
)
def test_is_order_valid(test_input, expected):
    rules, _ = load_data("Day_05/example_5a.txt")
    rules = proccess_rules(rules)
    assert is_order_valid(test_input, rules) == expected
