from task_11a import blink
import pytest


@pytest.mark.parametrize(
    "test_input, blink_num, expected",
    [
        (
            ["0", "1", "10", "99", "999"],
            1,
            ["1", "2024", "1", "0", "9", "9", "2021976"],
        ),
        (["125", "17"], 1, ["253000", "1", "7"]),
        (["125", "17"], 2, ["253", "0", "2024", "14168"]),
        (["125", "17"], 3, ["512072", "1", "20", "24", "28676032"]),
        (["125", "17"], 4, ["512", "72", "2024", "2", "0", "2", "4", "2867", "6032"]),
        (
            ["125", "17"],
            5,
            [
                "1036288",
                "7",
                "2",
                "20",
                "24",
                "4048",
                "1",
                "4048",
                "8096",
                "28",
                "67",
                "60",
                "32",
            ],
        ),
        (
            ["125", "17"],
            6,
            [
                "2097446912",
                "14168",
                "4048",
                "2",
                "0",
                "2",
                "4",
                "40",
                "48",
                "2024",
                "40",
                "48",
                "80",
                "96",
                "2",
                "8",
                "6",
                "7",
                "6",
                "0",
                "3",
                "2",
            ],
        ),
    ],
)
def test_blink(test_input, blink_num, expected):
    assert blink(test_input, blink_num) == expected
