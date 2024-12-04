import re


def load_instructions(filename):
    content = ""
    with open(filename, "r") as f:
        content = f.read()
    return content


def extract_instructions(instructions):
    # remove part between don't() and do()
    instruction = re.sub(r"don't\(\).*?do\(\)", "", instructions, flags=re.DOTALL)

    return re.findall(r"mul\(\d+,\d+\)", instruction)


if __name__ == "__main__":
    content = load_instructions("puzzle_input.txt")
    instructions = extract_instructions(content)
    total = 0
    for instruction in instructions:
        a, b = map(int, re.findall(r"\d+", instruction))
        total += a * b
    print(total)
