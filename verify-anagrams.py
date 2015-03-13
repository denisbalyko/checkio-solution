"""
def verify_anagrams(first_word, second_word):
    return sorted(first_word.replace(" ","").lower()) == sorted(second_word.replace(" ","").lower())
"""

func = lambda t: sorted(t.replace(" ", "").lower())
verify_anagrams = lambda f, s: func(f) == func(s)

if __name__ == '__main__':
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"
