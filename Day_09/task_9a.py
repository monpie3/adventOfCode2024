from collections import OrderedDict


def load_map(filename):
    with open(filename, "r") as f:
        return f.read().strip()


def unpack_disk(disk_map):
    disk_dict = OrderedDict()
    file_id = 0
    unwrap_id = 0
    for disk_id, repeat_num in enumerate(disk_map):
        repeat_num = int(repeat_num)

        for i in range(unwrap_id, unwrap_id + repeat_num):
            if disk_id % 2 == 0:
                disk_dict[i] = file_id  # file
            else:
                disk_dict[i] = "."  # space

        if disk_id % 2 == 0:
            file_id += 1
        unwrap_id += repeat_num

    return disk_dict


def compress(disk_dict):
    space_blocks = [i for i in disk_dict if disk_dict[i] == "."]

    ind_from_left = len(disk_dict) - 1
    for space in space_blocks:
        # find value to replace
        while disk_dict[ind_from_left] == "." and ind_from_left > 0:
            ind_from_left -= 1

        if space > ind_from_left:
            break

        disk_dict[space] = disk_dict[ind_from_left]
        disk_dict[ind_from_left] = "."

    return disk_dict


def get_checksum(compressed_dict):
    total = 0
    for ind, file_id in compressed_dict.items():
        if file_id != ".":
            total += ind * file_id
    return total


if "__main__" == __name__:
    disk_map = load_map("Day_09/puzzle_input.txt")
    disk_dict = unpack_disk(disk_map)
    compressed_dict = compress(disk_dict)
    checksum = get_checksum(compressed_dict)
    print(checksum)
