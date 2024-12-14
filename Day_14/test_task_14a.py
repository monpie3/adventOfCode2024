from task_14a import load_data, predit_motion, split_by_quadrant

WIDTH = 11
LENGTH = 7


def test_predict_motion():
    robots_dict = load_data("Day_14/example_14a.txt")
    prediction = predit_motion(robots_dict, 100, LENGTH, WIDTH)
    robots_by_quadrant = split_by_quadrant(prediction, LENGTH, WIDTH)
    assert [len(quadrant) for quadrant in robots_by_quadrant.values()] == [1, 3, 4, 1]
