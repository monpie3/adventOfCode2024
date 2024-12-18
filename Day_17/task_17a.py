import math


def load_data(filename):
    with open(filename, "r") as file:
        registers, program = file.read().split("\n\n")

    registers = [int(register.split(": ")[1]) for register in registers.split("\n")]
    program = program.strip().split(": ")[1].split(",")
    return registers, list(map(int, program))


def run_program(program, registers):

    def combo(operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        raise ValueError(f"Invalid operand: {operand}")

    a, b, c = registers

    output = []
    pointer = 0
    while pointer < len(program) - 1:
        jumped = False
        instruction = program[pointer]
        operand = program[pointer + 1]

        if instruction == 0:    # adv
            a = math.floor(a / pow(2, combo(operand)))
        elif instruction == 1:  # bxl
            b = b ^ operand
        elif instruction == 2:  # bst
            b = combo(operand) % 8
        elif instruction == 3:  # jnz
            if a != 0:
                pointer = operand
                jumped = True
        elif instruction == 4:  # bxc
            b = b ^ c
        elif instruction == 5:  # out
            output.append(combo(operand) % 8)
        elif instruction == 6:  # bdv
            b = math.floor(a / pow(2, combo(operand)))
        elif instruction == 7:  # cdv
            c = math.floor(a / pow(2, combo(operand)))

        if not jumped:
            pointer += 2

    return output, a, b, c


if __name__ == "__main__":
    registers, program = load_data("Day_17/puzzle_input.txt")
    output, a, b, c = run_program(program, registers)
    print(",".join(map(str, output)))
