import functools


def load_data(filename):
    with open(filename) as file:
        towels, designs = file.read().split("\n\n")

    towels = [towel for towel in towels.split(", ")]
    return towels, designs.strip().split("\n")


def count_valid_designs(towels, designs):

    @functools.cache
    def is_design_valid(design, index=0):
        if index == len(design):
            # we were able to check whole pattern of towels, so it is valid
            return True

        # we have to check all possible patterns of towels until true
        for towel in towels:
            if design[index:].startswith(towel):
                # check if the rest of the design is valid
                if is_design_valid(design, index + len(towel)):
                    return True

        # we coudn't find the combination of towels that would match the design
        return False

    valid = 0
    for design in designs:
        valid += is_design_valid(design)

    return valid


if __name__ == "__main__":
    towels, designs = load_data("Day_19/puzzle_input.txt")
    valid = count_valid_designs(towels, designs)
    print(valid)
