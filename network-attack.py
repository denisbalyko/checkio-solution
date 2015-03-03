from operator import itemgetter

def capture(matrix):
    queue, watched = [[0, 0]], [0]
    while len(queue):
        min_point = min(queue, key = itemgetter(1))
        queue.pop(queue.index(min_point))
        point, old_value = min_point
        for i, value in enumerate(matrix[point]):
            if value and not i == point and not i in watched:
                matrix[i][i] = matrix[i][i] + matrix[point][point]
                queue.append([i, matrix[i][i]])
                watched.append(i)

    return max(map(max, matrix))


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
