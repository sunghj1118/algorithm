# Initialize 5x5 board
board = [list(map(int, input().split())) for _ in range(5)]


def dfs(x, y, depth, curr_str):
    # base case
    if depth == 6:
        # add to set to ensure uniqueness
        result.add(curr_str)
        return

    # recursive case
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, depth+1, curr_str+str(board[nx][ny]))


# initialize set to store results
result = set()

# Choose random starting point to start dfs
for i in range(5):
    for j in range(5):
        dfs(i, j, 1, str(board[i][j]))

# print result
print(len(result))
