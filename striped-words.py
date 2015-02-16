import string
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    ans, text, vowels, consonants = 0, text.lower(), VOWELS.lower(), CONSONANTS.lower()

    for i in range(1,len(text)):
        if text[i] in string.punctuation:
            text = text.replace(text[i], " ")

    for word in text.split():
        if len(word)>1:
            w1 = word[::2]
            w2 = word[1::2]
            if set(w1).issubset(set(string.ascii_letters)) and  set(w2).issubset(set(string.ascii_letters)):
                if set(w1).issubset(set(vowels)) and set(w2).issubset(set(consonants)):
                    ans = ans + 1
                if set(w2).issubset(set(vowels)) and set(w1).issubset(set(consonants)):
                    ans = ans + 1
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(u"My name is ...") == 3, "All words are striped"
    #assert checkio(u"Hello world") == 0, "No one"
    #assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
