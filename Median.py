"""
def checkio(data):
    data.sort()
    center = int(len(data) / 2)
    if not (len(data) % 2):
        return (data[center]+data[center-1])/2
    else:
        return data[center]
"""
checkio = lambda data: (sorted(data)[int(len(sorted(data))/2)]+float(sorted(data)[int(len(sorted(data))/2)-1]))/2 if not (len(sorted(data)) % 2) else sorted(data)[int(len(sorted(data))/2)]


def test_function():
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")

