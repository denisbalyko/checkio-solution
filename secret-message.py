"""
def find_message(text):
    ans = ""
    for t in text:
        if t == t.upper() and t.isalpha():
            ans += t
    return ans
"""

find_message = lambda text: "".join([t for t in text if t == t.upper() and t.isalpha()])


def test_function():
    assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

if __name__ == '__main__':
    test_function()
