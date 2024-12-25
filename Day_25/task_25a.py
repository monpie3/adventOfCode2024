def load_data(filename):
    with open(filename) as file:
        content = file.read().split("\n\n")

    schemes = [row.splitlines() for row in content]
    keys, locks = categorize_schemes(schemes)
    return keys, locks


def categorize_schemes(schemes):
    locks, keys = [], []

    for scheme in schemes:
        pins = count_pins(scheme)
        if scheme[0][0] == "#":
            locks.append(pins)
        else:
            keys.append(pins)
    return keys, locks


def count_pins(scheme):
    counter = dict()
    for row_index in range(len(scheme)):
        if row_index != 0 and row_index != len(scheme) - 1:
            for col_index in range(len(scheme[row_index])):
                if col_index not in counter:
                    counter[col_index] = 0

                if scheme[row_index][col_index] == "#":
                    counter[col_index] += 1
    return [counter[pin] for pin in sorted(counter)]


def try_keys(keys, locks):
    max_height = len(locks[0])
    # try every key with every lock
    fit = 0
    for key in keys:
        for lock in locks:
            key_in_lock = [l + k for l, k in zip(lock, key)]
            if max(key_in_lock) <= max_height:
                fit += 1
    return fit


if __name__ == "__main__":
    keys, locks = load_data("Day_25/puzzle_input.txt")
    fit = try_keys(keys, locks)
    print(fit)
