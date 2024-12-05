from task_4b import (
    load_word_search,
    count_x_mass,
)


class TestCountXMAS(object):
    def test_on_dots(self):
        word_search = load_word_search("Day_04/example_4a.txt")
        assert count_x_mass(word_search) == 0

    def test_on_letters(self):
        word_search = load_word_search("Day_04/example_4b.txt")
        assert count_x_mass(word_search) == 9
