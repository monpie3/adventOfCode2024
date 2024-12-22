from task_22a import mix, prune, generate_new_secret


def test_mix():
    assert mix(42, 15) == 37


def test_prune():
    assert prune(100000000) == 16113920


def test_generate_new_secret():
    assert generate_new_secret(123) == 15887950
    assert generate_new_secret(123, 2) == 16495136
    assert generate_new_secret(123, 3) == 527345
    assert generate_new_secret(123, 4) == 704524
    assert generate_new_secret(123, 5) == 1553684
    assert generate_new_secret(123, 6) == 12683156
    assert generate_new_secret(123, 7) == 11100544
    assert generate_new_secret(123, 8) == 12249484
    assert generate_new_secret(123, 9) == 7753432
    assert generate_new_secret(123, 10) == 5908254


def test_generate_2000_new_secret():
    assert generate_new_secret(1, 2000) == 8685429
    assert generate_new_secret(10, 2000) == 4700978
    assert generate_new_secret(100, 2000) == 15273692
    assert generate_new_secret(2024, 2000) == 8667524
