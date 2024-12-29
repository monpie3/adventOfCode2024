from task_20a import load_map, cheat_threshold

import pytest


@pytest.mark.parametrize(
    "threshold,expected",
    [
        (64, 1),
        (40, 2),
        (38, 3),
        (36, 4),
        (20, 5),
        (12, 8),
        (10, 10),
        (8, 14),
        (6, 16),
        (4, 30),
        (2, 44),
    ],
)
def test_cheat_threshold(threshold, expected):
    racetrack = load_map("Day_20/example_20a.txt")
    pos = cheat_threshold(racetrack, threshold)
    assert len(pos) == expected
