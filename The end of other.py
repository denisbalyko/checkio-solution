def checkio(words_set):
    for w1 in words_set:
        for w2 in words_set:
            if not(w1 == w2) and (w1.endswith(w2)):
                return True
    return False

def test_function():
    assert checkio({u"hello", u"lo", u"he"}) is True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) is False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) is True, "duck to walk"
    assert checkio({u"one"}) is False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) is False, "Only end"

if __name__ == '__main__':
    test_function()
