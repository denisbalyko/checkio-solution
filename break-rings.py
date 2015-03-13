import itertools


def break_rings(rings):
    link_map = {}
    for link in rings:
        for ring in link:
            link_map.setdefault(ring, link.copy()).update(link)

    for i in range(1, len(link_map)):
        for destroy_rings in itertools.combinations(link_map.keys(), i):
            destroyed = set(destroy_rings)
            link_count = 0
            for links in link_map.items():
                if links[0] not in destroyed:
                    link_count += len(links[1] - destroyed) - 1
            if link_count == 0:
                return i


def test_function():
    assert break_rings(
        ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})
    ) == 3, "example"
    assert break_rings(
        ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})
    ) == 3, "All to all"
    assert break_rings(
        ({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})
    ) == 2, "Chain"
    assert break_rings(
        ({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})
    ) == 5, "Long chain"
    assert break_rings(
        ({1, 9}, {1, 2}, {8, 5}, {4, 6}, {5, 6}, {8, 1}, {3, 4},
         {2, 6}, {9, 6}, {8, 4}, {8, 3}, {5, 7}, {9, 7}, {2, 3}, {1, 7})
    ) == 5, "4/4"

if __name__ == '__main__':
    test_function()
