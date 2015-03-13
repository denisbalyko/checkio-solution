VOWELS = "aeiouy"


def translate(phrase):
    list_vowels, i = list(VOWELS), 0
    while i < len(phrase):
        if phrase[i] == " ":
            i = i + 1
            continue
        if phrase[i] in list_vowels:
            try:
                pass
                if phrase[i] == phrase[i+1] and phrase[i+1] == phrase[i+2]:
                    phrase = phrase[:i+1] + phrase[i+3:]
            except IndexError, e:
                raise e
        else:
            try:
                phrase = phrase[:i+1] + phrase[i+2:]
            except IndexError, e:
                pass
        i = i + 1
    return phrase


def test_function():
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

if __name__ == '__main__':
    test_function()
