import itertools


def load_map(filename):
    with open(filename, "r") as f:
        map_data = f.read()

    return [list(row) for row in map_data.split()]


def extract_antennas(antennas_map):
    antenna_positions = {}
    for row_ind, row in enumerate(antennas_map):
        for col_ind, cell in enumerate(row):
            if cell.isalnum():
                antenna_positions.setdefault(cell, []).append((row_ind, col_ind))
    return antenna_positions


def calculate_possible_antinodes(pair, vector, max_row, max_col):
    vector_x, vector_y = vector
    first_x, first_y = pair[0]
    second_x, second_y = pair[1]

    possible_antinodes = [
        (first_x + vector_x, first_y + vector_y),
        (first_x - vector_x, first_y - vector_y),
        (second_x + vector_x, second_y + vector_y),
        (second_x - vector_x, second_y - vector_y),
    ]

    return [
        node
        for node in possible_antinodes
        if 0 <= node[0] < max_row and 0 <= node[1] < max_col and node not in pair
    ]


def find_antinodes(map_data):
    antennas_by_frequency = extract_antennas(map_data)
    max_row, max_col = len(map_data), len(map_data[0])
    antinodes = set()

    for frequency in antennas_by_frequency:
        pairs = itertools.combinations(antennas_by_frequency[frequency], 2)

        for pair in pairs:
            first_x, first_y = pair[0]
            second_x, second_y = pair[1]
            vector = (first_x - second_x, first_y - second_y)

            possible_antinodes = calculate_possible_antinodes(
                pair, vector, max_row, max_col
            )

            for node in possible_antinodes:
                antinodes.add(node)

    return antinodes


if "__main__" == __name__:
    antennas_map = load_map("Day_08/puzzle_input.txt")
    antinodes = find_antinodes(antennas_map)
    print(len(antinodes))
