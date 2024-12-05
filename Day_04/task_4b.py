def load_word_search(filename):
    word_search = ""
    with open(filename, "r") as f:
        word_search = f.read()

    return [list(row) for row in word_search.split()]


def up_left(row, col):
    return row + 1, col + 1


def up_right(row, col):
    return row + 1, col - 1


def down_left(row, col):
    return row - 1, col + 1


def down_right(row, col):
    return row - 1, col - 1


def count_x_mass(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    total = 0
    for i in range(rows):
        for j in range(cols):
            if word_search[i][j] == "A":
                x_1a,y_1a = up_left(i, j)
                x_1b,y_1b = down_right(i, j)

                x_2a,y_2a = up_right(i, j)
                x_2b,y_2b = down_left(i, j)

                if any(x < 0 for x in [x_1a, y_1a, x_1b, y_1b, x_2a, y_2a, x_2b, y_2b]):
                    continue
                if any(x >= rows for x in [x_1a, x_1b, x_2a, x_2b]):
                    continue
                if any(y >= cols for y in [y_1a, y_1b, y_2a, y_2b]):
                    continue

                if (word_search[x_1a][y_1a] == "M" and word_search[x_1b][y_1b] == "S") or (word_search[x_1a][y_1a] == "S" and word_search[x_1b][y_1b] == "M"):
                    if (word_search[x_2a][y_2a] == "M" and word_search[x_2b][y_2b] == "S") or (word_search[x_2a][y_2a] == "S" and word_search[x_2b][y_2b] == "M"):
                        total += 1

    return total


if __name__ == "__main__":
    word_search = load_word_search("Day_04/puzzle_input.txt")
    print(count_x_mass(word_search))
