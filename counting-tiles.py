import math


def checkio(radius):
    def dist(lxy):
        return lxy[0]*lxy[0] + lxy[1]*lxy[1]
    N, all_count, any_count = int(math.ceil(radius)), 0, 0
    for x in xrange(0, N+1):
        for y in xrange(0, N+1):
            sq = [[x, y], [x, y+1], [x+1, y], [x+1, y+1]]
            f_all = True
            f_any = False
            for s in sq:
                if f_all and dist(s) > radius**2:
                    f_all = False
                if not f_any and dist(s) < radius**2:
                    f_any = True
            if f_all:
                all_count = all_count + 1
            elif f_any:
                any_count = any_count + 1
    return [all_count*4, any_count*4]


def test_function():
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

if __name__ == '__main__':
    test_function()
