def checkio(words_set):
    for w1 in words_set:
        for w2 in words_set:
            if not(w1 == w2) and (w1.endswith(w2)):
                return True
    return False

print checkio({u"hello", u"lo", u"he"}) == True, "helLO"
print checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
print checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
print checkio({u"one"}) == False, "Only One"
print checkio({u"helicopter", u"li", u"he"}) == False, "Only end"