def load_word_search(filename):
    word_search = ""
    with open(filename, "r") as f:
        word_search = f.read()

    return [list(row) for row in word_search.split()]


def transpose(word_search):
    rows = len(word_search)
    cols = len(word_search[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = word_search[i][j]
    return transposed


def up_left(row, col):
    return row + 1, col + 1


def up_right(row, col):
    return row + 1, col - 1


def down_left(row, col):
    return row - 1, col + 1


def down_right(row, col):
    return row - 1, col - 1


def count_diagonal(word_search):
    rows = len(word_search)
    cols = len(word_search[0])

    def explore_direction(i_M, y_M, up_left, word_search):
        diagonal = 0
        i_M, y_M = up_left(i, j)
        if i_M >= 0 and i_M < rows and y_M >= 0 and y_M < cols:
            if word_search[i_M][y_M] == "M":
                i_A, y_A = up_left(i_M, y_M)
                if i_A >= 0 and i_A < rows and y_A >= 0 and y_A < cols:
                    if word_search[i_A][y_A] == "A":
                        i_S, y_S = up_left(i_A, y_A)
                        if i_S >= 0 and i_S < rows and y_S >= 0 and y_S < cols:
                            if word_search[i_S][y_S] == "S":
                                diagonal += 1
        return diagonal

    total = 0
    for i in range(rows):
        for j in range(cols):
            if word_search[i][j] == "X":
                total += explore_direction(i, j, up_left, word_search)
                total += explore_direction(i, j, up_right, word_search)
                total += explore_direction(i, j, down_left, word_search)
                total += explore_direction(i, j, down_right, word_search)

    return total


def count_XMAS(word_search):
    total = 0
    for row in word_search:
        row = "".join(row)
        total += row.count("XMAS")
        total += row.count("SAMX")
    return total


def count_XMAS_in_all_axes(word_search):
    horizontal = count_XMAS(word_search)
    vertical = count_XMAS(transpose(word_search))
    diagonal = count_diagonal(word_search)
    return horizontal + vertical + diagonal


if __name__ == "__main__":
    word_search = load_word_search("Day_04/puzzle_input.txt")
    print(count_XMAS_in_all_axes(word_search))
