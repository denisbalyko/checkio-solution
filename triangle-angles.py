from math import acos, degrees

get_angle = lambda a, b, c: round(degrees(acos((b*b+c*c-a*a)/(float(2*b*c)))))


def checkio(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return [0, 0, 0]
    return sorted([get_angle(a, b, c), get_angle(b, c, a), get_angle(c, a, b)])


def test_function():
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
