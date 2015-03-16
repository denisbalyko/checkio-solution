from itertools import permutations

"""
def checkio(data):
    min_answer = sum(data)
    for step in permutations(data):
        for cut in range(len(step)):
            hand_l = step[:cut]
            hand_r = step[cut:]
            if min_answer > abs(sum(hand_l)-sum(hand_r)):
                min_answer = abs(sum(hand_l)-sum(hand_r))
    return min_answer
"""

checkio = lambda data: min(map(min, [[abs(sum(step[:cut])-sum(step[cut:])) for cut in range(len(step))] for step in permutations(data)]))


def test_function():
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"

if __name__ == '__main__':
    test_function()
