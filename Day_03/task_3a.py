import re

def load_instructions(filename):
    content = ""
    with open(filename, "r") as f:
        content = f.read()
    return content

def extract_instructions(instructions):
    return re.findall(r'mul\(\d+,\d+\)', instructions)



if __name__ == "__main__":
    content = load_instructions("Day_01/puzzle_input.txt")
    instructions = extract_instructions(content)
    total = 0
    for instruction in instructions:
        a,b = map(int, re.findall(r'\d+', instruction))
        print(a,b)
        total += a * b
    print(total)
