from task_23a import load_data, find_set_of_tree_computers


def test_find_set_of_tree_computers():
    connections = load_data("Day_23/example_23a.txt")
    three_computers = find_set_of_tree_computers(connections)
    assert len(three_computers) == 12
    filtered = {fs for fs in three_computers if any(el[0] == "t" for el in fs)}
    assert len(filtered) == 7
