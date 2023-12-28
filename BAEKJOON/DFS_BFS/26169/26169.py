from collections import deque


def dfs(board, row, column, move_count, apple_count):
    # Stopping Conditions
    if apple_count >= 2:
        return 1
    if move_count > 3:
        return 0

    # check if current location is valid
    if row < 0 or row >= 5 or column < 0 or column >= 5 or board[row][column] == -1:
        return 0

    # Check for apple and mark as visited
    if board[row][column] == 1:
        apple_count += 1
    temp = board[row][column]
    board[row][column] = -1

    # Check four directions
    result = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        result = result or dfs(board, row+dx, column+dy,
                               move_count+1, apple_count)

    # Backtrack
    board[row][column] = temp
    return result


# create board
# 0: empty, 1: apple, -1: obstacle
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

# take input location of student
student_r, student_c = map(int, input().split())

# check if 2 apples under 3 moves is possible
print(dfs(board, student_r, student_c, 0, 0))
