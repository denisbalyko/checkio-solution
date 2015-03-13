def boolean(x, y, operation):
    if operation == u"conjunction":
        return int(x and y)
    elif operation == u"disjunction":
        return int(x or y)
    elif operation == u"implication": 
        return int(not x or y)
    elif operation == u"exclusive":
        return int((x + y) % 2)
    elif operation == u"equivalence":
        return int(x == y)


def test_function():
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"

if __name__ == '__main__':
    test_function()
