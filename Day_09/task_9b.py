import collections


def load_map(filename):
    with open(filename, "r") as f:
        return f.read().strip()


def unpack_disk(disk_map):
    disk_dict = collections.defaultdict(list)
    file_id, unwraped_id = 0, 0

    for disk_id, repeat_num in enumerate(disk_map):
        repeat_num = int(repeat_num)

        if disk_id % 2 == 0:  # file
            disk_dict[file_id] = list(range(unwraped_id, unwraped_id + repeat_num))
        else:  # space
            disk_dict["."].append(list(range(unwraped_id, unwraped_id + repeat_num)))

        if disk_id % 2 == 0:
            file_id += 1
        unwraped_id += repeat_num

    return disk_dict


def convert_to_str(disk_dict):
    max_ind = max(max(row) for row in disk_dict.values())
    disk_list = ["." for _ in range(0, max_ind + 1)]
    for file_id in disk_dict:
        for ind in disk_dict[file_id]:
            disk_list[ind] = file_id
    return "".join(map(str, disk_list))


def compress_whole_files(disk_dict):
    space_blocks = disk_dict["."]
    del disk_dict["."]
    file_blocks = disk_dict

    for file_id in reversed(sorted(file_blocks.keys())):
        file_block = file_blocks[file_id]
        file_len = len(file_block)
        for space_block in space_blocks:
            if (
                space_block
                and len(space_block) >= file_len
                and file_block[0] >= space_block[0]
            ):
                file_blocks[file_id] = space_block[:file_len]
                # space not available anymore
                del space_block[:file_len]
                break

    return disk_dict


def get_checksum(compressed_dict):
    total = 0
    for file_id, indices in compressed_dict.items():
        for ind in indices:
            total += ind * file_id
    return total


if "__main__" == __name__:
    disk_map = load_map("Day_09/puzzle_input.txt")
    disk_dict = unpack_disk(disk_map)

    compressed_dict = compress_whole_files(disk_dict)
    checksum = get_checksum(compressed_dict)
    print(checksum)
