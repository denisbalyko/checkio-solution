checkio = lambda number: str(bin(number)).count("1")


def test_function():
    assert checkio(4) == 1, "4->1"
    assert checkio(15) == 4, "15->4"
    assert checkio(1) == 1, "1->1"
    assert checkio(1022) == 9, "1022->9"

if __name__ == '__main__':
    test_function()
