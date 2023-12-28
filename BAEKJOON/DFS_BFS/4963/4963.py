# dfs function
def dfs_iterative(i, j):
    stack = [(i, j)]

    while stack:
        x, y = stack.pop()
        if 0 <= x < H and 0 <= y < W and my_map[x][y] == 1:
            my_map[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                stack.append((x + dx, y + dy))

# input
# line 1: width, height
# line 2: for h rows, take map input
# last line: 0 0


W, H = 1, 1

# while W != 0 and H != 0:
while (W != 0 and H != 0):
    # initialize variables
    W, H = map(int, input().split())
    my_map = []
    island_count = 0

    if W == 0 and H == 0:
        break

    # get map input
    for _ in range(H):
        my_map.append(list(map(int, input().split())))

    # dfs search for islands
    for i in range(H):
        for j in range(W):
            if my_map[i][j] == 1:
                # mark all adjacent land as visited and erase them from map
                dfs_iterative(i, j)
                island_count += 1

    print(island_count)
