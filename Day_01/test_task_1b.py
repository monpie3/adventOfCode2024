from task_1b import read_file, similarity_score


def test_similarity_score():
    list_A, list_B = read_file("Day_01/example_1a.txt")
    assert similarity_score(list_A, list_B) == [9,4,0,0,9,9]
