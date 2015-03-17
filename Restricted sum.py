def checkio(data):
    if not data:
        return 0
    return data[0]+checkio(data[1:])


def test_function():
    assert checkio([1, 2, 3]) == 6, "6"
    assert checkio([2, 2, 2, 2, 2, 2]) == 12, "12"

if __name__ == '__main__':
    test_function()
