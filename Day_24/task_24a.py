def load_data(filename):
    with open(filename) as file:
        wire_inputs, gate_conn = file.read().split("\n\n")

    wire_inputs = [row.split(": ") for row in wire_inputs.splitlines()]
    wire_inputs = {row[0]: int(row[1]) for row in wire_inputs}

    gate_conn = [row.split(" -> ") for row in gate_conn.splitlines()]
    return wire_inputs, gate_conn


def simulate_gates(wire_inputs, gate_conn):
    while len(gate_conn) > 0:
        for row in gate_conn:
            inp, out = row
            x1, op, x2 = inp.split(" ")
            if x1 in wire_inputs and x2 in wire_inputs:
                match op:
                    case "AND":
                        wire_inputs[out] = wire_inputs[x1] & wire_inputs[x2]
                    case "OR":
                        wire_inputs[out] = wire_inputs[x1] | wire_inputs[x2]
                    case "XOR":
                        wire_inputs[out] = wire_inputs[x1] ^ wire_inputs[x2]
                gate_conn.remove(row)


def calculate_output(wire_inputs):
    filtered = {key: value for key, value in wire_inputs.items() if key.startswith("z")}

    num = ""
    for key in sorted(filtered.keys(), reverse=True):
        num += str(filtered[key])

    return num


if __name__ == "__main__":
    wire_inputs, gate_conn = load_data("Day_24/puzzle_input.txt")
    simulate_gates(wire_inputs, gate_conn)
    num = calculate_output(wire_inputs)
    print(num)
    print(int(num, 2))
