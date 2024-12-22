from task_22b import mix, prune, generate_new_secret, merge_dicts, load_data


def test_mix():
    assert mix(42, 15) == 37


def test_prune():
    assert prune(100000000) == 16113920


def test_generate_new_secret():
    repeat = 2000
    data = load_data("Day_22/example_22b.txt")
    merged_changes = dict()
    for secret in data:
        _, changes = generate_new_secret(secret, repeat)
        merge_dicts(merged_changes, changes)

    assert max(merged_changes, key=merged_changes.get) == (-2, 1, -1, 3)
    assert max(merged_changes.values()) == 23
