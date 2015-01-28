def checkio(words):
    i = 0
    for word in words.split():
        if word.isalpha():
            i += 1
        else:
            i = 0
        if i == 3:
            return True
    return False



print checkio("Hello World hello") == True, "Hello"
print checkio("He is 123 man") == False, "123 man"
print checkio("1 2 3 4") == False, "Digits"
print checkio("bla bla bla bla") == True, "Bla Bla"
print checkio("Hi") == False, "Hi"