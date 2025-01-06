from collections import defaultdict


def load_garden_data(filename):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    garden_dict = defaultdict(list)
    with open(filename, "r") as f:
        for row_ind, line in enumerate(f):
            for col_ind, plant in enumerate(line.strip()):
                connected = False

                regions = garden_dict[plant]
                for region in regions:
                    if any(
                        (row_ind + dx, col_ind + dy) in region for dx, dy in directions
                    ):
                        region.add((row_ind, col_ind))
                        connected = True

                if not connected:
                    garden_dict[plant].append({(row_ind, col_ind)})

        # if regions are connected then merge them
        # it can happen when we have something like:
        # . E
        # E E
        # (1,0) is not connected with (0,0), but
        # (1,1) is connected with (1,0) and (0,1)
        # so it will added to two regions
        for plant in garden_dict:
            regions = garden_dict[plant]
            garden_dict[plant] = merge_overlapping_sets(regions)

        return garden_dict


def merge_overlapping_sets(sets):
    merged = []

    for s in sets:
        overlapping = []
        for m in merged:
            if s & m:  # check for common elements
                overlapping.append(m)

        # remove overlapping sets and merge them into one
        for m in overlapping:
            merged.remove(m)
            s.update(m)

        # add the merged or original set to the result list
        merged.append(s)
    return merged


def how_many_neighbours(x, y, region):
    neighbours = 0
    if (x + 1, y) in region:
        neighbours += 1
    if (x - 1, y) in region and x - 1 >= 0:
        neighbours += 1
    if (x, y + 1) in region:
        neighbours += 1
    if (x, y - 1) in region and y - 1 >= 0:
        neighbours += 1

    return neighbours


def perimeter(points):
    p = 0
    for point_x, point_y in points:
        p += 4 - how_many_neighbours(point_x, point_y, points)
    return p


def calculate_price(garden):
    price = 0
    for plant in garden:
        area = garden[plant]

        for region in area:
            p = perimeter(region)
            price += len(region) * p

    return price


if "__main__" == __name__:
    garden = load_garden_data("Day_12/puzzle_input.txt")
    print(calculate_price(garden))
