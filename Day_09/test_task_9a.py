from task_9a import load_map, unpack_disk, compress, get_checksum
import pytest


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_09/example_9a.txt", "00...111...2...333.44.5555.6666.777.888899"),
        ("Day_09/example_9b.txt", "0..111....22222"),
    ],
)
def test_unpack_disk(file_path, expected):
    disk_map = load_map(file_path)
    disk_dict = unpack_disk(disk_map)
    unpacked = "".join(str(disk_dict[i]) for i in range(0, len(disk_dict)))
    # works because the file id is less than 10
    assert unpacked == expected


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_09/example_9a.txt", "0099811188827773336446555566.............."),
        ("Day_09/example_9b.txt", "022111222......"),
    ],
)
def test_compress(file_path, expected):
    disk_map = load_map(file_path)
    disk_dict = unpack_disk(disk_map)
    compressed_dict = compress(disk_dict)
    # works because the file id is less than 10
    compressed = "".join(
        str(compressed_dict[i]) for i in range(0, len(compressed_dict))
    )
    assert compressed == expected


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("Day_09/example_9a.txt", 1928),
        ("Day_09/example_9b.txt", 60),
    ],
)
def test_get_checksum(file_path, expected):
    disk_map = load_map(file_path)
    disk_dict = unpack_disk(disk_map)
    compressed_dict = compress(disk_dict)
    # works because the file id is less than 10
    assert get_checksum(compressed_dict) == expected
