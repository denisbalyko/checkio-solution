from string import ascii_letters, punctuation
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    ans, text = 0, text.lower()
    vowels, consonants = VOWELS.lower(), CONSONANTS.lower()

    for p in punctuation:
        text = text.replace(p, " ")

    for word in text.split():
        if len(word) > 1:
            odd = word[::2]
            even = word[1::2]
            if set(odd).issubset(set(ascii_letters)) and \
               set(even).issubset(set(ascii_letters)):
                if (set(odd).issubset(set(vowels)) and
                    set(even).issubset(set(consonants))) or \
                   (set(even).issubset(set(vowels)) and
                    set(odd).issubset(set(consonants))):
                    # odd-vow even-cons OR odd-cons even-vow
                    ans = ans + 1
    return ans


def test_function():
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

if __name__ == '__main__':
    test_function()
