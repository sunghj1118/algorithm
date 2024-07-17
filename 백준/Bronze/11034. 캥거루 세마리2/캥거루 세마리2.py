def jumps(a, b, c):
    positions = sorted([a, b, c])
    gap1 = positions[1] - positions[0] - 1
    gap2 = positions[2] - positions[1] - 1
    return max(gap1, gap2)

while True:
    try:
        a, b, c = map(int, input().split())
        print(jumps(a, b, c))
    except EOFError:
        break