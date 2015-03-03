# -*- coding: utf-8 -*-
def safe_pawns(pawns):
    def get_coord(cell):
        return ord(cell[0])-96, int(cell[1])

    # Получить клетки которые находятся под защитой
    def defend_coord(x, y):
        defend = []
        if (x+1 <= 8) and (y+1 <= 8):
            defend.append([x+1, y+1])
        if (x-1 <= 8) and (y+1 <= 8):
            defend.append([x-1, y+1])
        return defend

    # Пустая доска
    board = [[0 for j in range(9)] for i in range(9)]
    pawns, ans = list(pawns), 0

    # MAIN: пройти по клеткам и отметить все которые под защитой
    for pawn in pawns:
        for pwn in defend_coord(*get_coord(pawn)):
            board[pwn[0]][pwn[1]] = 1

    # Посчитать сумму клеток попавших под защищаемые
    for pawn in pawns:
        ans += board[get_coord(pawn)[0]][get_coord(pawn)[1]]
    return ans


def test_function():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"e8"}) == 0
