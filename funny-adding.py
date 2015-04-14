checkio = lambda data: sum(data)


def test_function():
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'

if __name__ == '__main__':
    test_function()
