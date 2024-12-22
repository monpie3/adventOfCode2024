def load_data(filename):
    with open(filename, "r") as file:
        return [int(row) for row in file.read().splitlines()]


def mix(secret, num):
    return secret ^ num


def prune(secret):
    return secret % 16777216


def generate_new_secret(old_secret, repeat=1):
    changes = dict()
    diff = []
    for _ in range(repeat):

        old_price = int(str(old_secret)[-1])
        new_secret = prune(mix(old_secret, old_secret * 64))
        new_secret = prune(mix(new_secret, int(new_secret / 32)))
        new_secret = prune(mix(new_secret, new_secret * 2048))

        old_secret = new_secret

        new_price = int(str(new_secret)[-1])

        if len(diff) == 4:
            diff.pop(0)

        diff.append(new_price - old_price)

        if len(diff) == 4:
            seq = tuple(diff)
            if seq in changes:
                continue  # monkey will only buy on the *first* sequence
            changes[seq] = new_price
    return new_secret, changes


def merge_dicts(merged, dict2):
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value


if __name__ == "__main__":
    data = load_data("Day_22/puzzle_input.txt")
    repeat = 2000

    merged_changes = dict()
    for secret in data:
        new_secret, changes = generate_new_secret(secret, repeat)
        merge_dicts(merged_changes, changes)

    print(max(merged_changes, key=merged_changes.get))
    print(max(merged_changes.values()))
