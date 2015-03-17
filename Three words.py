def checkio(words):
    i = 0
    for word in words.split():
        if word.isalpha():
            i += 1
        else:
            i = 0
        if i == 3:
            return True
    return False


def test_function():
    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"

if __name__ == '__main__':
    test_function()
