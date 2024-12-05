from task_5b import load_data, proccess_rules, fix_orders

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([[75, 97, 47, 61, 53]], [[97,75,47,61,53]]),
        ([[61, 13, 29]], [[61,29,13]]),
        ([[97, 13, 75, 29, 47]], [[97,75,47,29,13]]),
    ],
)
def test_is_order_valid(test_input, expected):
    rules, _ = load_data("Day_05/example_5a.txt")
    rules = proccess_rules(rules)
    assert fix_orders(test_input, rules) == expected
