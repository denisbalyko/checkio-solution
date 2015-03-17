"""
def left_join(phrases):
    return ",".join(phrases).replace('right', 'left')
"""

left_join = lambda p: ",".join(p).replace('right', 'left')


def test_function():
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"

if __name__ == '__main__':
    test_function()
