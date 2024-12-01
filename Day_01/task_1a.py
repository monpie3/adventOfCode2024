import re

def read_file(filename):
    list_A, list_B = [], []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().split("  ")
            list_A.append(line[0])
            list_B.append(line[1])
    return list_A, list_B

def total_distance(list_A, list_B):
    list_A = sorted(map(int, list_A))
    list_B = sorted(map(int, list_B))
    return [abs(a - b) for a, b in zip(list_A, list_B)]


if "__main__" == __name__:
    list_A, list_B = read_file("puzzle_input.txt")
    print(sum(total_distance(list_A, list_B)))
