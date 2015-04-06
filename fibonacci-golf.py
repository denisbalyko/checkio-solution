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
