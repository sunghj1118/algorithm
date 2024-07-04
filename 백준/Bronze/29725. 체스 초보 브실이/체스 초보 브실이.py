points = 0
for i in range(8):
    row = str(input())
    for c in row:
        if c == '.':
            pass
        # WHITE
        if c == 'K':
            pass
        if c == 'P':
            points = points + 1
        if c == 'N':
            points = points + 3
        if c == 'B':
            points = points + 3
        if c == 'R':
            points = points + 5
        if c == 'Q':
            points = points + 9
        # BLACK
        if c == 'k':
            pass
        if c == 'p':
            points = points - 1
        if c == 'n':
            points = points - 3
        if c == 'b':
            points = points - 3
        if c == 'r':
            points = points - 5
        if c == 'q':
            points = points - 9

print(points)