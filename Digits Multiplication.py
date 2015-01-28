"""
def checkio(number):
    multi = 1
    for num in str(number):
        if int(num):
            multi *= int(num)
    return multi
"""
checkio = lambda number: reduce(lambda res, x: res*x, [int(num) for num in str(number) if int(num)], 1)

print checkio(123405) == 120
print checkio(999) == 729
print checkio(1000) == 1
print checkio(1111) == 1
