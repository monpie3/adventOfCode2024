import functools


def load_data(filename):
    with open(filename) as file:
        towels, designs = file.read().split("\n\n")

    towels = [towel for towel in towels.split(", ")]
    return towels, designs.strip().split("\n")


def count_ways(towels, designs):

    @functools.cache
    def is_design_valid(design, index=0):
        combinations = 0

        if index == len(design):
            return 1

        for towel in towels:
            if design[index:].startswith(towel):
                combinations += is_design_valid(design, index + len(towel))

        return combinations

    return sum(map(is_design_valid, designs))


if __name__ == "__main__":
    towels, designs = load_data("Day_19/puzzle_input.txt")
    valid = count_ways(towels, designs)
    print(valid)
