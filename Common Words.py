"""
def checkio(first, second):
    s_first = set(first.split(","))
    s_second = set(second.split(","))
    return ",".join(sorted(s_first.intersection(s_second)))
"""

checkio = lambda first, second: ",".join(sorted(set(first.split(",")).intersection(set(second.split(",")))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
