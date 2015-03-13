def clock_angle(time):
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    deg_hour = ((hour % 12)*30 + 0.5*minute)
    deg_minute = (minute*6)

    if abs(deg_hour-deg_minute)<=180:
        return abs(deg_hour-deg_minute)
    else:
        return 360-abs(deg_hour-deg_minute)


def test_function():
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

if __name__ == '__main__':
    test_function()
