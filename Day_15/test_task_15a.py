from task_15a import load_data, find_robot_pos, move, find_boxes_pos
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_15/example_15a.txt", 10092),
        ("Day_15/example_15b.txt", 2028),
    ],
)
def test_find_trailhead(file_path, expected):
    warehouse_dic, robot_moves = load_data(file_path)
    current_pos = find_robot_pos(warehouse_dic)
    for direction in robot_moves:
        current_pos = move(warehouse_dic, current_pos, direction)
    boxes_pos = find_boxes_pos(warehouse_dic)
    assert sum([box[0] * 100 + box[1] for box in boxes_pos]) == expected
