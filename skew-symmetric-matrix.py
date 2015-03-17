def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j] == (-1)*matrix[j][i]:
                return False
    return True


def test_function():
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"

if __name__ == '__main__':
    test_function()
