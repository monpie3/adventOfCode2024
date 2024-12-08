from task_6a import load_lab_map, patrol


def test_patrol():
    lab_map = load_lab_map("Day_06/example_6a.txt")
    assert len(patrol(lab_map)) == 41


def test_patrol_when_guard_does_multiple_turns():
    # https://www.reddit.com/r/adventofcode/comments/1h8vq51/2024_day_6_part_2_i_am_stumped/
    lab_map = load_lab_map("Day_06/example_6b.txt")
    assert len(patrol(lab_map)) == 2
