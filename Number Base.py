def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1

print checkio("AF", 16) == 175, "Hex"
print checkio("101", 2) == 5, "Bin"
print checkio("101", 5) == 26, "5 base"
print checkio("Z", 36) == 35, "Z base"
print checkio("AB", 10) == -1, "B > A > 10"
