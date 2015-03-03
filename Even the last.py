def checkio(array):
    if array:
        return sum(array[::2])*array[-1]
    return 0

if [-45]:
    print [-45][-1]
    print [-45][::2]
else:
    print "321"


print checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
print checkio([1, 3, 5]) == 30, "(1+5)*5=30"
print checkio([6]) == 36, "(6)*6=36"
print checkio([]) == 0, "An empty array = 0"
print checkio([-45])
