import collections


def load_data(filename):
    connections = collections.defaultdict(set)
    content = []
    with open(filename) as file:
        content = [row.split("-") for row in file.read().splitlines()]

    for row in content:
        connections[row[0]].add(row[1])
        connections[row[1]].add(row[0])
    return connections


def find_set_of_tree_computers(connections):
    three_computers = set()
    for node in connections:
        for node_2 in connections[node]:
            # check if they have common connections
            common = connections[node_2].intersection(connections[node])
            for node_3 in common:
                three_computers.add(frozenset([node, node_2, node_3]))
    return three_computers


if __name__ == "__main__":
    connections = load_data("Day_23/puzzle_input.txt")
    three_computers = find_set_of_tree_computers(connections)
    filtered = {fs for fs in three_computers if any(el[0] == "t" for el in fs)}
    print(len(filtered))
