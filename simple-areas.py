import math


def simple_areas(*args):
    def circle(args):
        r = args[0]
        return float(math.pi*(r**2))/4

    def rectangle(args):
        a, b = args
        return a * b

    def triangle(args):
        a, b, c = args
        p = float(a + b + c)/2
        return (p*(p - a)*(p - b)*(p - c))**(float(1)/2)

    switch = {
        1: circle,
        2: rectangle,
        3: triangle
    }
    return switch[len(args)](args)


def test_function():
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(1000), 785398.16), "Big Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

if __name__ == '__main__':
    test_function()
