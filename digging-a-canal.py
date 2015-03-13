import copy


def checkio(matrix):
    counts, L = [], len(matrix[0])
    for i in range(L):
        for j in range(L):
            coord = [0, i, len(matrix) - 1, j]
            count = get_last_point(copy.deepcopy(matrix), *coord)
            counts.append(count)
    return min(counts)


def pop_min(labyrinth, queue):
    min_q = [labyrinth[q[0]][q[1]] for q in queue]
    min_point = min_q.index(min(min_q))
    return queue.pop(min_point)


def get_last_point(labyrinth, xn, yn, xk, yk):
    """Initial Values"""
    queue = []
    queue.append([xn, yn])
    N, M = len(labyrinth), len(labyrinth[0])
    watched = [[False for jj in range(M)] for ii in range(N)]
    watched[xn][yn] = True

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


def test_last_point():
    assert get_last_point([[0, 0, 1], [1, 2, 3], [1, 2, 3]], 0, 0, 2, 2) == 7, "3x3 diagonal"
    """
    [
        [0, 0, 1],
        [1, 2, 4],
        [2, 4, 7],
    ]
    """
    assert get_last_point([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0, 2, 2) == 5, "3x3 ones"
    """
    [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ]
    """
    assert get_last_point([[10, 10], [10, 10]], 0, 0, 1, 1) == 30, "2x2 tens"
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
    ], 0, 0, 6, 6) == 8, "big ex"

    assert get_last_point([[1, 2, 3],
                           [1, 2, 3],
                           [1, 2, 3]], 0, 0, 2, 2) == 8, "3x3 ones"


def test_function():
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 10, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"
    assert checkio([[0, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 0]]) == 0, "horizontal range"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]) == 1,  "vertical range"


def test_pop_min():
    assert pop_min([[10, 10],
                    [10, 9]],
                    [[0, 0],
                     [1, 0],
                     [0, 1],
                     [1, 1]]) == [1, 1], "popmin"


if __name__ == '__main__':
    test_last_point()
    test_pop_min()
    test_function()
