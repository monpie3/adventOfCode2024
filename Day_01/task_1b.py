def read_file(filename):
    list_A, list_B = [], []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().split("  ")
            list_A.append(line[0])
            list_B.append(line[1])
    return list_A, list_B

def similarity_score(list_A, list_B):
    list_A = map(int, list_A)
    list_B = list(map(int, list_B))
    return [a * list_B.count(a) for a in list_A]


if "__main__" == __name__:
    list_A, list_B = read_file("puzzle_input.txt")
    print(sum(similarity_score(list_A, list_B)))
