import copy
import itertools
import json
import re

# import tqdm


def load_data(filename):
    data_dict = {}
    with open(filename, "r") as f:
        for ind, line in enumerate(f.readlines()):
            pos_y, pos_x, vel_y, vel_x = map(int, re.findall(r"[+-]?\d+", line))
            data_dict[ind] = {"pos": (pos_x, pos_y), "vel": (vel_x, vel_y)}
        return data_dict


def predit_motion(robots_dict, time, space_wide, space_tall):
    robots_dict = copy.deepcopy(robots_dict)
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


def create_robot_pos_map(robot_dict, length, width):
    map_data = [["." for _ in range(width)] for _ in range(length)]

    for robot in robot_dict.values():
        x, y = robot["pos"]
        map_data[x][y] = "#"

    map_data = ["".join(row) for row in map_data]
    map_data = "\n".join(map_data)
    # print(map_data)
    return map_data


def save_json_as_html(file_path):
    with open(file_path, "r") as file:
        map_data = json.load(file)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Easter egg</title>
        <style>
            body {
                font-family: monospace;
                background-color: #f4f4f4;
                color: #333;
                padding: 20px;
            }
            .container {
                display: flex;
                flex-wrap: wrap;
            }
            .map {
                margin-bottom: 10px;
                padding: 10px;
                background: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
                overflow-x: auto;
                white-space: pre;
            }
            .map pre {
                font-size: 3px;
            }
        </style>
    </head>
    <body>
        <h1>Data Map</h1>
        <div class="container">
    """

    # Add each block to the HTML
    for t, easter_egg in map_data.items():
        html_content += f"""
        <div class="map">
            <h3>Time: {t}</h3>
            <pre>{easter_egg}</pre>
        </div>
        """

    # Close HTML tags
    html_content += """
        </div>
    </body>
    </html>
    """

    # Save the HTML to a file
    output_file = "Day_14/day_14_limited.html"
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"HTML file generated: {output_file}")


if "__main__" == __name__:
    WIDTH = 101
    LENGTH = 103

    time_limit = WIDTH * LENGTH

    # robots vertically align every 101 steps from X = 9
    # and horizontally every 103 steps from Y = 65
    vertical_range = range(9, time_limit, WIDTH)
    horizontal_range = range(65, time_limit, LENGTH)
    limited_range = sorted(itertools.chain(vertical_range, horizontal_range))

    robots_dict = load_data("Day_14/puzzle_input.txt")
    map_data = {}

    for t in limited_range:
        # for t in tqdm.tqdm(range(1, time_limit)):
        prediction = predit_motion(robots_dict, t, LENGTH, WIDTH)
        map_data[t] = create_robot_pos_map(prediction, LENGTH, WIDTH)

    # save map data to json
    file_path = "Day_14/easter_egg_limited.json"
    with open(file_path, "w") as file:
        json.dump(map_data, file, indent=4)
    print(f"Map data saved to {file_path}")

    save_json_as_html(file_path)
