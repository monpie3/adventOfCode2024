from task_9b import (
    load_map,
    unpack_disk,
    compress_whole_files,
    get_checksum,
    convert_to_str,
)
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_09/example_9a.txt", "00992111777.44.333....5555.6666.....8888"),
        ("Day_09/example_9b.txt", "0..111....22222"),
        ("Day_09/example_9c.txt", "000331..222"),  # 000..1..222...33
        (
            "Day_09/example_9d.txt",
            "01",
        ),  # 121 -> 0..1  # https://www.reddit.com/r/adventofcode/comments/1hap2nq/2024_day_9_part_2_doubly_linked_madness_help/
        ("Day_09/example_9e.txt", "01"),  # 111 -> 0.1.
        ("Day_09/example_9g.txt", "000111"),  # 333 -> 000...111
    ],
)
def test_compress_whole_files(file_path, expected):
    disk_map = load_map(file_path)
    disk_dict = unpack_disk(disk_map)
    compressed_dict = compress_whole_files(disk_dict)
    compressed = convert_to_str(compressed_dict)
    assert compressed == expected


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_09/example_9a.txt", 2858),
        ("Day_09/example_9b.txt", 132),
        ("Day_09/example_9d.txt", 1),
        ("Day_09/example_9e.txt", 1),
        ("Day_09/example_9f.txt", 2910),
    ],
)
def test_get_checksum(file_path, expected):
    disk_map = load_map(file_path)
    disk_dict = unpack_disk(disk_map)
    compressed_dict = compress_whole_files(disk_dict)
    assert get_checksum(compressed_dict) == expected
