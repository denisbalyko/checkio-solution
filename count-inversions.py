def count_inversion(sequence):
    flag, answer, sequence = True, 0, list(sequence)
    while flag:
        flag = False
        for i in xrange(1, len(sequence)):
            if sequence[i-1] > sequence[i]:
                sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
                answer += 1
                flag = True
    return answer


def test_function():
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
