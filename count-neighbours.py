# -*- coding: utf-8 -*-
def count_neighbours(grid, row, col):

    directions = ((-1, 1), # ↖
                 (0, 1),  # ↑
                 (1, 1),  # ↗
                 (-1, 0), # ←
                 (1, 0),  # →
                 (-1, -1),# ↙
                 (0, -1), # ↓
                 (1, -1)  # ↘
                 )
    s = 0
    # want to go in directions / хотим пойти по направлениям
    for direct in directions:
        # check did not fall off the board / проверяем не упали ли с доски ?
        if (col+direct[0] >= 0) and (col+direct[0] < len(grid[0])) and \
           (row+direct[1] >= 0) and (row+direct[1] < len(grid)):
            # If ok, then adds content / Если ок, добавим содержимое
            s += grid[row+direct[1]][col+direct[0]]
    return s
