"""
def days_diff(date1, date2):
    from datetime import date
    return (abs(date(*date1)-date(*date2))).days
"""

from datetime import date
days_diff = lambda date1, date2: (abs(date(*date1)-date(*date2))).days


def test_function():
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
