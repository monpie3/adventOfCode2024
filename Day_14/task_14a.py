import functools
import operator
import re


def load_data(filename):
    data_dict = {}
    with open(filename, "r") as f:
        for ind, line in enumerate(f.readlines()):
            pos_y, pos_x, vel_y, vel_x = map(int, re.findall(r"[+-]?\d+", line))
            data_dict[ind] = {"pos": (pos_x, pos_y), "vel": (vel_x, vel_y)}
        return data_dict


def predit_motion(robots_dict, time, space_wide, space_tall):
    reduced_time_for_wide = time % space_wide
    reduced_time_for_tall = time % space_tall

    for robot in robots_dict:
        pos_x, pos_y = robots_dict[robot]["pos"]
        vel_x, vel_y = robots_dict[robot]["vel"]

        for _ in range(reduced_time_for_wide):
            pos_x = pos_x + vel_x
            if pos_x > space_wide - 1:
                pos_x = pos_x - space_wide
            if pos_x < 0:
                pos_x = space_wide + pos_x

        for _ in range(reduced_time_for_tall):
            pos_y = pos_y + vel_y
            if pos_y > space_tall - 1:
                pos_y = pos_y - space_tall
            if pos_y < 0:
                pos_y = space_tall + pos_y

        robots_dict[robot]["pos"] = (pos_x, pos_y)

    return robots_dict


def get_quadrant(pos_x, pos_y, middle_x, middle_y):
    if pos_x < middle_x and pos_y < middle_y:
        return "I"
    if pos_x < middle_x and pos_y > middle_y:
        return "II"
    if pos_x > middle_x and pos_y < middle_y:
        return "III"
    if pos_x > middle_x and pos_y > middle_y:
        return "IV"
    else:
        return None


def split_by_quadrant(robots_dict, space_wide, space_tall):
    # Assume that space_wide and space_tall are odd numbers
    middle_x = space_wide // 2
    middle_y = space_tall // 2

    robots_quadrant = {"I": [], "II": [], "III": [], "IV": []}

    for robot in robots_dict:
        pos_x, pos_y = robots_dict[robot]["pos"]
        quadrant = get_quadrant(pos_x, pos_y, middle_x, middle_y)
        if quadrant:  # Skip robots that are in the middle
            robots_quadrant[quadrant].append((pos_x, pos_y))
    return robots_quadrant


if "__main__" == __name__:
    WIDTH = 101
    LENGTH = 103

    robots_dict = load_data("Day_14/puzzle_input.txt")
    prediction = predit_motion(robots_dict, 100, LENGTH, WIDTH)
    robots_by_quadrant = split_by_quadrant(prediction, LENGTH, WIDTH)
    count_by_quadrant = [len(quadrant) for quadrant in robots_by_quadrant.values()]
    print(functools.reduce(operator.mul, count_by_quadrant))
