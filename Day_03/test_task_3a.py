from task_3a import load_instructions, extract_instructions


def test_extract_instructions():
    example = load_instructions("Day_03/example_3a.txt")
    assert extract_instructions(example) == ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
