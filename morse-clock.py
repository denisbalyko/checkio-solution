def checkio(time_string):
    def get_mask(number, count=4):
        res = ""
        root = (8, 4, 2, 1)[-count:]
        for r in root:
            if r <= number:
                res = res + "-"
                number = number - r
            else:
                res = res + "."
        return res

    result, data = [], [(x[:1], x[1:]) for x in time_string.split(':')]
    start_letter = True
    for first, second in data:
        if not second:
            first, second = 0, first
        count = 3
        if start_letter:
            start_letter = False
            count = 2
        result.append(get_mask(int(first), count) + " " + get_mask(int(second)))
    return " : ".join(result)


def test_function():
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
