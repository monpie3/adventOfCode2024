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


## Day 09
In part two, I got rid of `OrderedDict` since I hadn't  actually used it in part one anyway.
To improve performance, I changed the structure from `index: file_id` to `file_id: [list of indices]`, as searching through the old dictionary was painfully slow.
I also replaced the while loop with a for loop (always a pleasure) 😇

## Day 10
[![meme from day 10](/memes/day_10.png)](https://www.reddit.com/r/adventofcode/comments/1hbbtdd/2024_day_10/)

Been there, done that 😅


## Day 11
The choice of a dynamic list as a data container was not the best. It turns out that order was not important at all, and it would have been much better to use a hash map where the key would be the engraved number and the value the number of occurrences.

[![nicer solution for day 11](/memes/day_11.png)](https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1kau09/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)


I also read that returning from a `with` block (e.g., when opening a file) works fine, and the file is automatically closed. The `with` statement ensures cleanup happens, whether the block exits normally or via a return.  [🔗](https://stackoverflow.com/questions/9885217/in-python-if-i-return-inside-a-with-block-will-the-file-still-close)


## Day 12
I probably would have done better if my `puzzle_input` had been correct instead of last year's 😅
But this was one of those tasks I really liked (aside from the wrong input), where I had to grab a sheet of paper and a pen to plan it out.
What I’m proud of is that I came up with the correct perimeter formula right away. Even though it’s a bit basic, it works!

[![amazing trolling from JS](/memes/day_12.png)](https://www.reddit.com/r/adventofcode/comments/1hcyh1x/2024_day_12_when_your_code_is_a_standup_comedian/)

## Day 13
I didn't want to reinvent the wheel, so I just went with `sympy`. Two equations with two unknowns. It was fun to solve the test examples on paper.

[![meme partially about day 13](/memes/day_13.png)](https://xkcd.com/1838/)

## Day 14
In my case, searching for the Easter egg using the smallest safety factor didn’t work (though it turns out it was the *second* smallest result!). However, I listed all the possible cases, and after entering `5000` as an answer, I knew the range I should focus on (which at least halved my search efforts 😅).

I think it wasn’t the best idea to store robot positions as JSON. Using images with `PIL` would probably have been faster, but I wanted to avoid libraries that require additional installation (`tqdm` doesn’t count—it’s just a little helper to check if my program is still running).

I know some people enjoyed this task, but after browsing Reddit, I feel it’s too dependent on the input. I don’t like that someone might solve it just because they got lucky, rather than because their method works for everyone or because they caught on to something critical in the task’s description.

![my tree](memes/day_14.png.png)


## Day 17

The [match](https://docs.python.org/3/tutorial/controlflow.html#tut-match) statement is a more elegant alternative to `if...elif...else` ✨

## Day 18
[![meme from day 18](/memes/day_18.png)](https://www.reddit.com/r/adventofcode/comments/1hgz05a/2024_day_18_pinch_me_it_worked/)


Brute force was good enough, so I stuck with it. Apparently, you can practically reuse part 2 from day 16 (you just need to remove the condition about 1000 points → [🔗](https://www.reddit.com/r/adventofcode/comments/1hguacy/comment/m2q835j/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)), but I don’t have that part ready yet, so we’ll see in the future 😅

## Day 20
Part 1: I forgot that two picoseconds are needed for the cheating, so the distance isn’t simply the difference between the end position index and the start position index—we need to reduce it by 2.

