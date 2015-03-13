def solution1(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i+1][j]) and \
           (matrix[i][j] == matrix[i+2][j]) and \
           (matrix[i][j] == matrix[i+3][j]):
            return True
    except IndexError:
        return False

def solution2(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i][j+1]) and \
           (matrix[i][j] == matrix[i][j+2]) and \
           (matrix[i][j] == matrix[i][j+3]):
            return True
    except IndexError:
        return False

def solution3(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i-1][j-1]) and \
           (matrix[i][j] == matrix[i-2][j-2]) and \
           (matrix[i][j] == matrix[i-3][j-3]):
            if (i-1 < 0)or(i-2 < 0)or(i-3 < 0)or(j-1 < 0)or(j-2 < 0)or(j-3 < 0):
                return False
            return True
    except IndexError:
        return False

def solution4(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i-1][j+1]) and \
           (matrix[i][j] == matrix[i-2][j+2]) and \
           (matrix[i][j] == matrix[i-3][j+3]):
            if (i-1 < 0)or(i-2 < 0)or(i-3 < 0):
                return False
            return True
    except IndexError:
        return False


def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if solution1(matrix, i, j) or solution2(matrix, i, j) or \
               solution3(matrix, i, j) or solution4(matrix, i, j):
                return True
    return False


def test_function():
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1, 5, 4, 4],
        [2, 2, 4, 1],
        [1, 4, 3, 5],
        [4, 3, 3, 2]
    ]) == True, "test4/4"
    assert checkio([
        [2,6,2,2,7,6,5],
        [3,4,8,7,7,3,6],
        [6,7,3,1,2,4,1],
        [2,5,7,6,3,2,2],
        [3,4,3,2,7,5,6],
        [8,4,6,5,2,9,7],
        [5,8,3,1,3,7,8]
    ]) == False, "test5/5"
    assert checkio([
        [2,3,6,5,6,2,8,3,7,4],
        [6,9,5,9,7,6,8,5,1,6],
        [6,8,2,6,1,9,3,6,6,4],
        [5,8,3,2,3,8,7,4,6,4],
        [2,3,1,4,5,1,2,5,6,9],
        [5,4,8,7,5,5,8,4,9,5],
        [9,7,9,9,5,9,9,8,1,2],
        [5,1,7,4,8,3,4,1,8,8],
        [5,3,3,2,6,1,4,3,8,8],
        [4,8,1,4,5,8,8,7,4,7]
    ])