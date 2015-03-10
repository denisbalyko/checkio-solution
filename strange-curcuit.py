import math


get_matrix = lambda size, v: [[v for j in range(size)] for i in range(size)]
get_size = lambda a, b: int(math.ceil(math.sqrt(max(a, b))))
get_start_pos = lambda size: (int(math.floor(float(size) / 2)), int(math.floor(float(size) / 2 - 0.5)))
is_fin = lambda spiral: all([all(i) for i in spiral])


def find_distance(first, second):
    N = get_size(first, second)
    onematrix = get_matrix(N, 1)
    spiral = get_spiral(N)
    for i in range(N):
        for j in range(N):
            if spiral[i][j] == first:
                xn, yn = i, j
            if spiral[i][j] == second:
                xk, yk = i, j
    return get_last_point(onematrix, xn, yn, xk, yk)


def get_spiral(size):
    spiral = get_matrix(size, 0)
    xn, yn = get_start_pos(size)
    counter = 1
    spiral[xn][yn] = counter
    xn = xn - 1
    directs = ((1, 0), (0, -1), (-1, 0), (0, 1))
    while not is_fin(spiral):
        for i, direct in enumerate(directs):
            look_dx, look_dy = direct
            look_x, look_y = xn + look_dx, yn + look_dy

            dx, dy = directs[i-1]
            xx, yy = xn + dx, yn + dy

            while (look_x >= 0) and (look_y >= 0) and \
                  (look_x < len(spiral)) and (look_y < len(spiral)) and \
                    bool(spiral[look_x][look_y]):

                counter += 1
                if spiral[xn][yn] > 0:
                    break
                spiral[xn][yn] = counter
                look_x, look_y = xx + look_dx, yy + look_dy
                if (xx >= 0) and (yy >= 0) and \
                   (xx < len(spiral)) and (yy < len(spiral)):
                    xn, yn = xx, yy
                    xx, yy = xx + dx, yy + dy
                else:
                    break
    return spiral


def get_last_point(labyrinth, xn, yn, xk, yk):
    """Initial Values"""
    queue = []
    queue.append([xn, yn])
    N, M = len(labyrinth), len(labyrinth[0])
    watched = [[False for jj in range(M)] for ii in range(N)]
    watched[xn][yn] = True
    labyrinth[xn][yn] = 0

    """Create path"""
    while queue:
        xn, yn = pop_min(labyrinth, queue)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = xn + dx, yn + dy
            if  (x >= 0) and (x < N) and \
                (y >= 0) and (y < M) and \
                not watched[x][y]:
                queue.append([x, y])
                watched[x][y] = True
                labyrinth[x][y] = labyrinth[x][y] + labyrinth[xn][yn]

    """Return LastPoint"""
    return labyrinth[xk][yk]


def pop_min(labyrinth, queue):
    min_q = [labyrinth[q[0]][q[1]] for q in queue]
    min_point = min_q.index(min(min_q))
    return queue.pop(min_point)


def test_pop_min():
    assert pop_min([[10, 10],
                    [10, 9]],
                    [[0, 0],
                     [1, 0],
                     [0, 1],
                     [1, 1]]) == [1, 1], "popmin"


def test_size():
    assert get_size(1, 2) == 2, "2"
    assert get_size(4, 5) == 3, "3"
    assert get_size(50, 2) == 8, "8"
    assert get_size(100, 2) == 10, "4"


def test_spiral():
    assert get_spiral(2) == [[2, 3], [1, 4]], "spiral2x2"
    assert get_spiral(3) == [[9, 2, 3], [8, 1, 4], [7, 6, 5]], "spiral3x3"


def test_start_pos():
    assert get_start_pos(2) == (1, 0), "2x2"
    assert get_start_pos(3) == (1, 1), "3x3"
    assert get_start_pos(4) == (2, 1), "4x4"
    assert get_start_pos(5) == (2, 2), "5x5"


def test_is_fin():
    assert is_fin([[1, 1], [1, 1]]) is True, "end"
    assert is_fin([[0, 0], [0, 0]]) is False, "start"
    assert is_fin([[1, 1], [0, 1]]) is False, "preend"


def test_last_point():
    assert get_last_point([[0, 0, 1], [1, 2, 3], [1, 2, 3]], 0, 0, 2, 2) == 7, "3x3 diagonal"
    """
    [
        [0, 0, 1],
        [1, 2, 4],
        [2, 4, 7],
    ]
    """
    assert get_last_point([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0, 2, 2) == 4, "3x3 ones"
    """
    [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ]
    """
    assert get_last_point([[10, 10], [10, 10]], 0, 0, 1, 1) == 20, "2x2 tens"
    """
    [
        [10, 20],
        [20, 30],
    ]
    """
    assert get_last_point([
        [1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1]
    ], 0, 0, 6, 6) == 7, "big ex"

    assert get_last_point([[1, 2, 3],
                           [1, 2, 3],
                           [1, 2, 3]], 0, 0, 2, 2) == 7, "3x3 ones"


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"

if __name__ == '__main__':
    test_size()
    test_pop_min()
    test_is_fin()
    test_start_pos()
    test_spiral()
    test_function()
    test_last_point()
