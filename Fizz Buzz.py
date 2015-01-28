def checkio(number):
    if number % 15 == 0:
        return "Fizz Buzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)

print checkio(15) == "Fizz Buzz"
print checkio(6) == "Fizz"
print checkio(5) == "Buzz"
print checkio(7) == "7"