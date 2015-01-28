def checkio(data):
    if not data:
        return 0
    return data[0]+checkio(data[1:])

checkio([1, 2, 3]) == 6
checkio([2, 2, 2, 2, 2, 2]) == 12