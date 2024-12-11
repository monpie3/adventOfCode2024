def load_stones(filename):
    with open(filename, "r") as f:
        return f.read().strip().split(" ")


def blink(stones, blink_num):
    for _ in range(blink_num):
        offset = 0
        for ind in range(len(stones)):

            engraved_stone = stones[ind + offset]
            # print(f"{engraved_stone=}")
            if engraved_stone == "0":
                # print("0->1")
                stones[ind + offset] = "1"

            elif len(engraved_stone) % 2 == 0:
                # print("split stones")
                new_stone_p1 = engraved_stone[: len(engraved_stone) // 2]
                new_stone_p2 = (
                    engraved_stone[len(engraved_stone) // 2 :].lstrip("0") or "0"
                )

                stones[ind + offset] = new_stone_p1
                stones.insert(ind + offset + 1, new_stone_p2)
                offset += 1
            else:
                # print("X->X*2024")
                stones[ind + offset] = str(int(engraved_stone) * 2024)
        # print("-- NEXT BLINK --")
    # print("OUTPUT: ", stones)
    return stones


if "__main__" == __name__:
    stones = load_stones("Day_11/puzzle_input.txt")
    print(len(blink(stones, 25)))
