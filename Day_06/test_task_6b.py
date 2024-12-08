from task_6b import (
    load_lab_map,
    patrol,
    add_obstructions,
    find_guard_position,
    find_guard_direction,
)


def test_patrol():
    lab_map = load_lab_map("Day_06/example_6a.txt")
    start_position = find_guard_position(lab_map)
    start_direction = find_guard_direction(lab_map, start_position)
    assert len(patrol(lab_map, start_position, start_direction)[0]) == 41


def test_patrol_when_guard_does_multiple_turns():
    # https://www.reddit.com/r/adventofcode/comments/1h8vq51/2024_day_6_part_2_i_am_stumped/
    lab_map = load_lab_map("Day_06/example_6b.txt")
    start_position = find_guard_position(lab_map)
    start_direction = find_guard_direction(lab_map, start_position)
    assert len(patrol(lab_map, start_position, start_direction)[0]) == 2


def test_add_obstration():
    lab_map = load_lab_map("Day_06/example_6a.txt")
    start_position = find_guard_position(lab_map)
    start_direction = find_guard_direction(lab_map, start_position)
    current_area = patrol(lab_map, start_position, start_direction)[0]
    del current_area[start_position]
    assert add_obstructions(lab_map, current_area, start_position, start_direction) == 6


def test_add_obstration_when_guard_does_multiple_turns():
    lab_map = load_lab_map("Day_06/example_6c.txt")
    start_position = find_guard_position(lab_map)
    start_direction = find_guard_direction(lab_map, start_position)
    current_area = patrol(lab_map, start_position, start_direction)[0]
    del current_area[start_position]
    assert add_obstructions(lab_map, current_area, start_position, start_direction) == 0
