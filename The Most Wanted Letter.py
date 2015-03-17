import re


def checkio(text):
    maxcol, maxcolCurrent, maxsymb, maxsymbLast = 0, 0, '', ''
    for s in sorted(text.lower()):
        if not re.search('[a-z]+', s):
            continue
        maxsymbCurrent = s
        if maxsymbLast != maxsymbCurrent:
            maxcolCurrent = 1
        else:
            maxcolCurrent += 1
        if maxcolCurrent > maxcol:
            maxsymb, maxcol = maxsymbCurrent, maxcolCurrent
        maxsymbLast = s
    return maxsymb


def test_function():
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

if __name__ == '__main__':
    test_function()
