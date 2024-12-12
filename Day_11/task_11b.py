import functools


def load_stones(filename):
    with open(filename, "r") as f:
        return map(int, f.read().strip().split(" "))


def process_stone(engraved_stone):
    if engraved_stone == 0:
        return [1]

    str_stone = str(engraved_stone)
    if len(str_stone) % 2 == 0:
        half_len = len(str_stone) // 2
        return [int(str_stone[:half_len]), int(str_stone[half_len:])]
    return [engraved_stone * 2024]


@functools.cache
def blink_for_single_stone(stone, blink_num):
    new_stones = process_stone(stone)
    if blink_num == 1:
        return len(new_stones)  # either one or two
    else:
        return sum(blink_for_single_stone(stone, blink_num - 1) for stone in new_stones)


def blink(stones, blink_num):
    # process_stone(125) + process_stone(17) == process_stone([125, 17])
    total = 0
    for stone in stones:
        total += blink_for_single_stone(stone, blink_num)
    return total


if "__main__" == __name__:
    stones = load_stones("Day_11/puzzle_input.txt")
    print(blink(stones, 75))
