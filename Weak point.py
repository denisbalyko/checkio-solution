def weak_point(matrix):
    minSumLine_i, minSumLine_j = 101, 101
    tr_matrix = map(list, zip(*matrix))
    for i in range(len(matrix)):
        if minSumLine_i > sum(matrix[i]):
            minSumLine_i = sum(matrix[i])
            i_min = i
        if minSumLine_j > sum(tr_matrix[i]):
            minSumLine_j = sum(tr_matrix[i])
            j_min = i

    return i_min, j_min  # [0, 0]


def test_function():
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
