import math

def checkio(data):
    def io(digit):
        if isinstance(digit, int):
            return str(digit)
        else:
            return "%.2f" % digit
    d = []
    for item in data.split(","):
        for l_item in item.split("("):
            if l_item:
                try:
                    d.append(int(l_item))
                except ValueError:
                    pass
        for r_item in item.split(")"):
            if r_item:
                try:
                    d.append(int(r_item))
                except ValueError:
                    pass

    x1,y1,x2,y2,x3,y3 = d[0],d[1],d[2],d[3],d[4],d[5]

    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2*(A*(y3-y2)-B*(x3-x2))
    if G == 0:
        return
    x = (D * E - B * F) / G
    y = (A * F - C * E) / G
    """
    ma = (y2-y1)/(x2-x1)
    mb = (y3-y2)/(x3-x2)

    x = (ma*mb*(y1-y3) + mb*(x1+x2) - ma*(x2+x3))/(2*(mb-ma))
    if not ma == 0:
        y = (-1/ma)*(x-(x1+x2)/2)+(y1+y2)/2
    else:
        y = (-1/mb)*(x-(x2+x3)/2)+(y2+y3)/2
    """


    r = math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
    print "(x-{0})^2+(y-{1})^2={2}^2".format(io(x), io(y), "%.2f" % r)
    return "(x-{0})^2+(y-{1})^2={2}^2".format(io(x), io(y), "%.2f" % r)


if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
