# adventOfCode2024 🎄

[![Python application](https://github.com/monpie3/adventOfCode2024/actions/workflows/python.yml/badge.svg)](https://github.com/monpie3/adventOfCode2024/actions/workflows/python.yml) [![codecov](https://codecov.io/gh/monpie3/adventOfCode2024/graph/badge.svg?token=sJt7iNyDHN)](https://codecov.io/gh/monpie3/adventOfCode2024)

You can find the puzzle inputs here: [https://adventofcode.com/2024](https://adventofcode.com/2024)

### Recap of my progress in Advent of Code so far:

-   [2023](https://github.com/monpie3/adventOfCode2023): 22 days (36 ⭐)
-   [2020](https://github.com/monpie3/adventOfCode2020): 10 days (19 ⭐)

# What have I learned this year?

## Day 1

-   How to use Git credential store on WSL → [🔗](https://stackoverflow.com/questions/45925964/how-to-use-git-credential-store-on-wsl-ubuntu-on-windows)
-   How to change the default editor from nano to vim → [🔗](https://askubuntu.com/questions/539243/how-to-change-visudo-editor-from-nano-to-vim)

## Day 2

[![meme from day 2](/memes/day_02.png)](https://www.reddit.com/r/adventofcode/comments/1h4pelm/2024_day_2_part_2_the_actual_elves_in_part_2/)

## Day 3

-   A good reminder that `.` by default matches any character except a new line. So, I learned about [DOTALL](https://docs.python.org/3/library/re.html#re.DOTALL) flag.
-   I came across this website: https://regexcrossword.com/

[![meme from day 3](/memes/day_03.png)](https://www.reddit.com/r/adventofcode/comments/1h5uhsu/2024_day_3_summarized_in_one_picture/)

## Day 4

[![meme from day 4](/memes/day_04.png)](https://www.reddit.com/r/adventofcode/comments/1h6bls8/2024_day_4_part_2_small_misunderstanding/)

## Day 5

- The better solution is to use sorting with a custom comparator function →

[![better solution for day 5](/memes/day_05.png)](https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0k8gc1/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)


## Day 6

-   Used `time python Day_06/task_6b.py` to measure the execution time of the script

[![meme from day 6](/memes/day_06.png)](https://www.reddit.com/r/adventofcode/comments/1h8o6d0/how_do_you_handle_this/)

[![secend meme from day 6](/memes/day_06-2.png)](https://www.reddit.com/r/adventofcode/comments/1h7v2n5/2024_day_6_part_2_that_wont_cause_a_time_paradox/)

## Day 7

-   The go-to solution: `itertools.product`

[![meme from day 7](/memes/day_07.png)](https://www.reddit.com/r/adventofcode/comments/1h8xiga/2024_aoc_is_the_year_of_bruteforcing_anyway/)

## Day 8

- Using the next iterator from [`itertools`](https://docs.python.org/3/library/itertools.html) → `combinations`

- A cleaner way to handle this kind of logic. Instead of writing:
```
if cell not in antenna_positions:
    antenna_positions[cell] = [(row_ind, col_ind)]
else:
    antenna_positions[cell].append((row_ind, col_ind))
```
We can refactor it to be more concise:
`antenna_positions.setdefault(cell, []).append((row_ind, col_ind))`

Alternatively, we can use `defaultdict` from `collections`, which automatically provides a default value for the key that doesn't exist.
