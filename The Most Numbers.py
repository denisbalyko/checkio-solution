checkio=lambda *args: max(args)-min(args) if args else 0

def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


def test_function():
    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"

if __name__ == '__main__':
    test_function()
