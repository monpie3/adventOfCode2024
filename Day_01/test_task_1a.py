from task_1a import read_file, total_distance


def test_total_distance():
    list_A, list_B = read_file("Day_01/example_1a.txt")
    assert total_distance(list_A, list_B) == [2, 1, 0, 1, 2, 5]
