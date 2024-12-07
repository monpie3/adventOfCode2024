from task_6a import load_lab_map, patrol


def test_patrol():
    lab_map = load_lab_map("Day_06/example_6a.txt")
    assert len(patrol(lab_map)) == 41
