from fractions import gcd


def greatest_common_divisor(*args):
    args = list(args)
    a, b = args.pop(), args.pop()
    gcd_local = gcd(a, b)
    while len(args):
        gcd_local = gcd(gcd_local, args.pop())
    return gcd_local


def test_function():
    assert greatest_common_divisor(6, 10, 15) == 1, "12"
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

if __name__ == '__main__':
    test_function()
