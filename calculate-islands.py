# -*- coding: utf-8 -*-

directions = ((-1, 1),   # ↖
              (0, 1),    # ↑
              (1, 1),    # ↗
              (-1, 0),   # ←
              (1, 0),    # →
              (-1, -1),  # ↙
              (0, -1),   # ↓
              (1, -1))   # ↘


def checkio(land_map):
    ans_list = []
    for i in range(len(land_map)):
        for j in range(len(land_map[0])):
            if land_map[i][j] > 0:
                ans_list.append(get_count_island(land_map, i, j))
    return sorted(ans_list)


def get_count_island(land_map, i, j):
    queue = [(i, j)]
    maxlen, land_map[i][j] = 1, -1
    while queue:
        xn, yn = queue.pop()
        for dx, dy in directions:
            x, y = xn + dx, yn + dy
            if (x >= 0) and (y >= 0) and \
               (x < len(land_map)) and (y < len(land_map[0])) and \
               (land_map[x][y] > 0):
                land_map[x][y] = -1
                queue.append((x, y))
                maxlen += 1
    return maxlen


def test_get_count_island():
    assert get_count_island([[1]], 0, 0) == 1, "one"
    assert get_count_island([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0) == 9, "all"
    assert get_count_island([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 0, 0) == 8, "without center"
    assert get_count_island([[0, 0], [1, 1]], 1, 1) == 2, "last two"


def test_function():
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"

if __name__ == '__main__':
    test_function()
    test_get_count_island()
