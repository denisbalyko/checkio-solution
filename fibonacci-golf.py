def fibgolf(t, n):
    I, o, l  = [1]*3, [0, 1], [1, 2]
    s = {'ib': (o, l, I),'ri': (o + [1], l + [3], I),'uc': ([2, 1], l, I),'ac': (o, l, l + [1]),'el': (o, l, [2, 1, 1]),'er': ([3, 0, 2], [2, 3], I),'ad': (o + [1], [2, 3], I)}
    a, F, m = s[t[1:3]]
    while len(a)<n+2: a.append(sum([m[i]*a[-d] for i, d in enumerate(F)]))
    return a[n]


def test_function():
    assert fibgolf(u'fibonacci', 10) == 55
    assert fibgolf(u'tribonacci', 10) == 149
    assert fibgolf(u'lucas', 10) == 123
    assert fibgolf(u'jacobsthal', 10) == 341
    assert fibgolf(u'pell', 10) == 2378
    assert fibgolf(u'perrin', 10) == 17
    assert fibgolf(u'padovan', 10) == 9

if __name__ == '__main__':
    test_function()

"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149,
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123,
0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341,
0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378,
3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22,
1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28
"""
