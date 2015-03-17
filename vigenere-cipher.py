def decode_vigenere(od, oe, ne):
    m, key, key_raw = 0, "", "".join([chr(65 + (ord(oe[i])-ord(od[i])+26) % 26) for i in range(len(oe))])

    def make_slicer(key, length):
        slicer = key * (length // len(key) + 1)
        return slicer[:length]

    def take_key(slicer):
        for i in range(1, len(slicer)+1):
            if make_slicer(slicer[:i], len(slicer)) == slicer:
                return slicer[:i]

    key = take_key(key_raw)

    return "".join([chr(65 + (ord(ne[i])-ord(key[i % len(key)])) % 26) for i in range(len(ne))])


def test_function():
    assert decode_vigenere(u'DONTWORRYBEHAPPY',
                           u'FVRVGWFTFFGRIDRF',
                           u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
    assert decode_vigenere(u'LOREMIPSUM',
                           u'OCCSDQJEXA',
                           u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
