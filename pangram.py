# why do I read? :( http://www.checkio.org/blog/pangram-review/
from string import ascii_lowercase

"""
def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))
"""

check_pangram = lambda t: set(ascii_lowercase).issubset(set(t.lower()))


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
