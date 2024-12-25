from task_25a import load_data, try_keys


def test_try_keys():
    keys, locks = load_data("Day_25/example_25a.txt")
    fit = try_keys(keys, locks)
    assert fit == 3
