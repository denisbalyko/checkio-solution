import types


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    m_val = None
    if not key:
        key = lambda x: x
    if len(args) == 2:
        a, b = args
        if a > b:
            return b
        else:
            return a
    if len(args) == 1:
        args = args[0]
    if isinstance(args, types.GeneratorType):
        m = args.next()
    elif isinstance(args, set):
        args = list(args)
        m = key(args[0])
    else:
        m = key(args[0])
        m_val = args[0]
    for arg in args:
        if key(arg) < m:
            m = key(arg)
            m_val = arg
    return m_val


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    m_val = None
    if not key:
        key = lambda x: x
    if len(args) == 2:
        a, b = args
        if a < b:
            return b
        else:
            return a
    if len(args) == 1:
        args = args[0]
    if isinstance(args, types.GeneratorType):
        m = args.next()
        m_val = m
    elif isinstance(args, set):
        args = list(args)
        m = key(args[0])
    else:
        m = key(args[0])
        m_val = args[0]
    for arg in args:
        if key(arg) > m:
            m = key(arg)
            m_val = arg
    return m_val




print max(3, 2) == 3
print min(3, 2) == 2
print max([1, 2, 0, 3, 4]) == 4
print min("hello") == "e"
print max(2.2, 5.6, 5.9, key=int) == 5.6
print min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
print min(abs(i) for i in range(-10, 10)) == 0
print max(abs(i) for i in range(-10, 10)) == 10

print min({1, 2, 3, 4, -10}) == -10
print max({1, 2, 3, 4, -10}) == 4
