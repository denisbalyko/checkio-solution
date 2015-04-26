def checkio(numbers):
    queue = [(0, numbers), ]
    max_total = -10000
    while queue:
        current_total, current_tail = queue.pop(0)
        for _ in xrange(0, 2):
            if len(current_tail) > 0:
                next_step = current_tail.pop(0)
                next_tail = current_tail[:]
                queue.append((current_total+next_step, next_tail),)
            else:
                max_total = max(max_total, current_total)
    return max_total


def test_function():
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'

if __name__ == '__main__':
    test_function()
