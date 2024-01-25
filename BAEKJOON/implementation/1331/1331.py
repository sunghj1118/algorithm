def check(prev, next, visited):
    """Check if pos is visited and if it is possible to move to pos"""
    # need to check if visited
    if visited[next[0]][next[1]]:
        return False

    # need to check if possible to move
    if abs(prev[0] - next[0]) == 2 and abs(prev[1] - next[1]) == 1:
        return True
    elif abs(prev[0] - next[0]) == 1 and abs(prev[1] - next[1]) == 2:
        return True
    else:
        return False


def translate(pos):
    """Translates chess language position to index
    translate chess language to index
    ex) A1 -> (0, 0), B1 -> (0, 1), A2 -> (1, 0), ...
    """
    letter = pos[0]
    num = int(pos[1])

    mapping = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5
    }

    if letter in mapping:
        return (num - 1, mapping[letter])
    else:
        return (-1, -1)


# input
visited = [[False] * 6 for _ in range(6)]
prev = (0, 0)
flag = True

for i in range(36):
    pos = input()
    pos = translate(pos)

    if i == 0:  # first input
        first_pos = pos
        visited[first_pos[0]][first_pos[1]] = True
        prev = pos
        pass
    elif i == 35:  # last input
        # need to check if possible to move to first position
        if abs(pos[0] - first_pos[0]) == 2 and abs(pos[1] - first_pos[1]) == 1:
            visited[pos[0]][pos[1]] = True
            pass
        elif abs(pos[0] - first_pos[0]) == 1 and abs(pos[1] - first_pos[1]) == 2:
            visited[pos[0]][pos[1]] = True
            pass
        else:
            flag = False
            break
    elif check(prev, pos, visited):  # check if possible to move
        visited[pos[0]][pos[1]] = True
        prev = pos
    else:
        flag = False
        break

# check if all positions are visited
if flag and all(all(row) for row in visited):
    print("Valid")
else:
    print("Invalid")
