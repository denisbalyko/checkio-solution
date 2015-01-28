checkio = lambda number: str(bin(number)).count("1")

print checkio(4) == 1
print checkio(15) == 4
print checkio(1) == 1
print checkio(1022) == 9