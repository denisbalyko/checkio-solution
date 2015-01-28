__author__ = 'denisbalyko'


def checkio(labyrinth):
    queue, answer = [], ""
    xn, yn = 1, 1               #start_position
    start_value = 10            #(any greater than 0 and 1)
    queue.append([xn, yn])
    labyrinth[xn][yn] = start_value
    """Create path"""
    while queue:
        xn, yn = queue.pop(0)
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xk, yk = xn + x, yn + y
            if (xk > 0) and (xk < 12) and (yk > 0) and (yk < 12) and (labyrinth[xk][yk] == 0):
                queue.append([xk, yk])
                labyrinth[xk][yk] = labyrinth[xn][yn] + 1
    """Back to home"""
    xn, yn = 10, 10             #end_position
    while not (labyrinth[xn][yn] == start_value):
        for x, y, direct in [(1, 0, "N"), (-1, 0, "S"), (0, 1, "W"), (0, -1, "E")]:
            xk, yk = xn + x, yn + y
            if labyrinth[xn][yn] == labyrinth[xk][yk] + 1:
                xn, yn = xk, yk
                answer = direct + answer
                break

    return answer


print checkio([[1,1,1,1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,1,0,1,1,1],
               [1,0,1,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,1,1,1,1,1,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,1],
               [1,0,0,0,1,1,0,1,1,1,0,1],
               [1,0,1,0,0,0,0,1,0,1,1,1],
               [1,0,1,1,0,1,0,0,0,0,0,1],
               [1,0,1,0,0,1,1,1,1,1,0,1],
               [1,0,0,0,1,1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1]])

print checkio([[1,1,1,1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,1,0,1,1,1],
               [1,0,1,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,1,1,1,1,1,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,1],
               [1,0,0,0,1,1,0,1,1,1,0,1],
               [1,0,1,0,0,0,0,1,0,1,1,1],
               [1,0,1,1,0,1,0,0,0,0,0,1],
               [1,0,1,0,0,1,1,1,1,1,0,1],
               [1,0,0,0,1,1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1]]) == "SSSSSEENNNEEEEEEESSWWWWSSSEEEESS"