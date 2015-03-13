def letter_queue(commands):
    stack = []
    for command in commands:
        if command == 'POP':
            if stack:
                stack.pop(0)
        else:
            letter = command.split()[1]
            stack.append(letter)
    return "".join(stack)


def test_function():
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
