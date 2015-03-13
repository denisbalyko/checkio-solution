def checkio(n, m):
    return bin(n ^ m).count('1')


def test_function():
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
