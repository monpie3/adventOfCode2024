from task_17a import load_data, run_program
import pytest


@pytest.mark.parametrize(
    "file_path, exp_a, exp_b, exp_c, exp_output",
    [
        ("Day_17/example_17a.txt", "X", "X", "X", "4,6,3,5,6,3,5,2,1,0"),
        ("Day_17/example_17b.txt", "X", 1, "X", "X"),
        ("Day_17/example_17c.txt", "X", "X", "X", "0,1,2"),
        ("Day_17/example_17d.txt", 0, "X", "X", "4,2,5,6,7,7,7,7,3,1,0"),
        ("Day_17/example_17e.txt", "X", 26, "X", "X"),
        ("Day_17/example_17f.txt", "X", 44354, "X", "X"),
    ],
)
def test_run_programe(file_path, exp_a, exp_b, exp_c, exp_output):
    registers, program = load_data(file_path)
    output, a, b, c = run_program(program, registers)

    if exp_a != "X":
        assert a == exp_a

    if exp_b != "X":
        assert b == exp_b

    if exp_c != "X":
        assert c == exp_c

    if exp_output != "X":
        assert ",".join(map(str, output)) == exp_output
