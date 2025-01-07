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


def count_sides(region):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # right and down, right and up, left and down and left and up

    num_corners = 0
    for point_x, point_y in region:
        for row_offset, col_offset in directions:
            row_neighbor = (point_x + row_offset, point_y)
            col_neighbor = (point_x, point_y + col_offset)
            diagonal_neighbor = (point_x + row_offset, point_y + col_offset)

            if row_neighbor not in region and col_neighbor not in region:
                # outside corner
                num_corners += 1

            if (
                row_neighbor in region
                and col_neighbor in region
                and diagonal_neighbor not in region
            ):
                # inside corner
                num_corners += 1
    return num_corners


def calculate_price(garden):
    price = 0
    for plant in garden:
        area = garden[plant]
        for region in area:
            s = count_sides(region)
            price += len(region) * s

    return price


if "__main__" == __name__:
    garden = load_garden_data("Day_12/puzzle_input.txt")
    print(calculate_price(garden))
