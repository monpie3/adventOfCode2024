def load_data(filename):
    with open(filename, "r") as file:
        return [int(row) for row in file.read().splitlines()]


def mix(secret, num):
    return secret ^ num


def prune(secret):
    return secret % 16777216


def generate_new_secret(old_secret, repeat=1):
    for _ in range(repeat):
        num = old_secret * 64
        new_secret = mix(old_secret, num)
        new_secret = prune(new_secret)

        num = int(new_secret / 32)
        new_secret = mix(new_secret, num)
        new_secret = prune(new_secret)

        num = new_secret * 2048
        new_secret = mix(new_secret, num)
        new_secret = prune(new_secret)

        old_secret = new_secret
    return new_secret


if __name__ == "__main__":
    data = load_data("Day_22/puzzle_input.txt")
    total = 0
    for secret in data:
        total += generate_new_secret(secret, 2000)
    print(total)
