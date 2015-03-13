def digit_stack(commands):
    stack, answer = [], 0

    for command in commands:
        if command == "POP":
            answer += stack.pop() if stack else 0

        if command == "PEEK":
            answer += stack[-1] if stack else 0

        if command.startswith("PUSH"):
            stack.append(int(command.split(" ")[1]))
    return answer


def test_function():
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
