import datetime


def checkio(from_date, to_date):
    SATUDAY, SUNDAY, ans = 6, 7, 0
    for i in range((to_date-from_date).days + 1):
        if from_date.isoweekday() == SATUDAY or from_date.isoweekday() == SUNDAY:
            ans = ans + 1
        from_date = from_date + datetime.timedelta(days=1)
    return ans


def test_function():
    assert checkio(datetime.date(2013, 9, 18), datetime.date(2013, 9, 23)) == 2, "1st example"
    assert checkio(datetime.date(2013, 1, 1), datetime.date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(datetime.date(2013, 2, 2), datetime.date(2013, 2, 3)) == 2, "3rd example"
