from task_3b import load_instructions, extract_instructions


def test_extract_instructions():
    example = load_instructions("Day_03/example_3b.txt")
    assert extract_instructions(example) == ['mul(2,4)', 'mul(8,5)']
