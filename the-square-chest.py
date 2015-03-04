dimension = 4


def checkio(matrix):
    ans = 0
    for i in range(16):
        for n in next_number(i + 1):
            flag = True
            xn, yn = get_coord(i + 1)
            xk, yk = get_coord(n)
            for side in matrix_sort(conversion(get_allside(xn, yn, xk, yk))):
                if flag and not side in matrix_sort(matrix):
                    flag = False
            if flag:
                ans = ans + 1
    return ans


def get_side(xn, yn, xk, yk):
    if xn == xk:
        return [[[xn, yn+i], [xk, yn+i+1]] for i in range(abs(yn-yk))]
    if yn == yk:
        return [[[xn+i, yn], [xn+i+1, yk]] for i in range(abs(xn-xk))]
    return None


def conversion(list_side):
    return [[get_number(side[0]), get_number(side[1])] for side in list_side]


def matrix_sort(matrix):
    return [[el[0], el[1]] if el[0]>el[1] else [el[1], el[0]] for el in matrix]


def get_allside(xn, yn, xk, yk):
    return get_side(xn, yn, xk, yn) + \
           get_side(xk, yn, xk, yk) + \
           get_side(xn, yk, xk, yk) + \
           get_side(xn, yn, xn, yk)


def next_number(number):
    return {
        1: [6, 11, 16],
        2: [7, 12],
        3: [8],
        4: [],
        5: [10, 15],
        6: [11, 16],
        7: [12],
        8: [],
        9: [14],
        10: [15],
        11: [16],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
    }[number]


def get_coord(number):
    number = number - 1
    return (number // dimension, number % dimension)


def get_number(coord):
    x, y = coord
    return x * 4 + y + 1


def test_coord():
    assert get_coord(1) == (0, 0), u"1 number"
    assert get_coord(5) == (1, 0), u"5 number"
    assert get_coord(15) == (3, 2), u"15 number"
    assert get_coord(16) == (3, 3), u"16 number"


def test_number():
    assert get_number((0, 0)) == 1, u"1 number"
    assert get_number((1, 0)) == 5, u"5 number"
    assert get_number((3, 2)) == 15, u"15 number"
    assert get_number((3, 3)) == 16, u"16 number"
    assert get_number(get_coord(10)) == 10, u"in 10"


def test_allside():
    assert get_allside(0, 0, 1, 1) == [
        [[0,0],[1,0]],
        [[1,0],[1,1]],
        [[0,1],[1,1]],
        [[0,0],[0,1]]
    ], "00 11"


def test_side():
    assert get_side(1, 1, 3, 1) == [
        [[1,1],[2,1]],
        [[2,1],[3,1]],
    ], u"2 line vert"
    assert get_side(0, 2, 3, 2) == [
        [[0,2],[1,2]],
        [[1,2],[2,2]],
        [[2,2],[3,2]],
    ], u"4 line vert"
    assert get_side(2, 0, 2, 3) == [
        [[2,0],[2,1]],
        [[2,1],[2,2]],
        [[2,2],[2,3]],
    ], u"4 line horizont"
    assert get_side(0, 0, 2, 2) == None, u"None side"


def test_function():
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert (checkio([[16, 15], [16, 12], [15, 11],
                     [11, 12], [11, 10], [10, 14],
                     [9, 10], [14, 13], [13, 9], [15, 14]]) == 3), "Last"


if __name__ == '__main__':
    test_coord()
    test_number()
    test_side()
    test_allside()
    test_function()
