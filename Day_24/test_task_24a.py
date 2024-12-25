from task_24a import load_data, simulate_gates, calculate_output


def test_calculate_output():
    wire_inputs, gate_conn = load_data("Day_24/example_24a.txt")
    simulate_gates(wire_inputs, gate_conn)
    num = calculate_output(wire_inputs)
    assert num == "100"
    assert int(num, 2) == 4
