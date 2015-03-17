def recursion(matrix, i, j, value):
    if (i >= 0) and (j >= 0) and (i < len(matrix)) and (j < len(matrix)) and (matrix[i][j] == value):
        matrix[i][j] = 0
        return 1+recursion(matrix, i + 1, j, value)+\
                 recursion(matrix, i - 1, j, value)+\
                 recursion(matrix, i, j + 1, value)+\
                 recursion(matrix, i, j - 1, value)
    else:
        return 0


def checkio(matrix):
    count, val = [],[]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]:
                v = matrix[x][y]
                val.append(v)
                count.append(recursion(matrix, x, y, v))
    id = count.index(max(count))
    return [count[id], val[id]]


def test_function():
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'

    assert checkio([
        [4,4,4,4,4,3,4],
        [2,3,4,4,4,4,4],
        [2,4,4,5,4,4,3],
        [4,2,2,4,1,2,4],
        [3,4,1,4,4,4,5],
        [4,4,2,4,4,2,4],
        [3,4,4,4,4,4,2]
    ]) == [15,4], '15 of 4'

if __name__ == '__main__':
    test_function()
