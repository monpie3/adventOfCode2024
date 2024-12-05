from task_4a import (
    load_word_search,
    count_XMAS_in_all_axes,
)


class TestCountXMASInAllAxes(object):
    def test_on_dots(self):
        word_search = load_word_search("Day_04/example_4a.txt")
        assert count_XMAS_in_all_axes(word_search) == 4

    def test_on_letters(self):
        word_search = load_word_search("Day_04/example_4b.txt")
        assert count_XMAS_in_all_axes(word_search) == 18
