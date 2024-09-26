def dp(dp_table, x1,y1,x2,y2):
    # x2,y2 is the sum of all values from 0,0 to x2,y2
    big_rectangle = dp_table[x2][y2]

    # x1,y1 is the sum of all values from 0,0 to x1,y1
    up_rectangle = dp_table[x1-1][y2]

    # x1,y2 is the sum of all values from 0,0 to x1,y2
    left_rectangle = dp_table[x2][y1-1]

    # x2,y1 is the sum of all values from 0,0 to x2,y1
    overlap_rectangle = dp_table[x1-1][y1-1]

    # By cutting the rectangle from x1,y1 to x2,y2, we can get the sum of the rectangle
    sum = big_rectangle - left_rectangle - up_rectangle + overlap_rectangle
    return sum

n,m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# intialize dp table
dp_table = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]

# base case
dp_table[0][0] = grid[0][0]

# fill all the rectangle sums for the dp table
for i in range(1, len(grid)+1):
    for j in range(1, len(grid)+1):
        dp_up = dp_table[i-1][j] if i > 0 else 0
        dp_left = dp_table[i][j-1] if j > 0 else 0
        dp_diag = dp_table[i-1][j-1] if i > 0 and j > 0 else 0
        dp_table[i][j] = dp_up + dp_left + grid[i-1][j-1] - dp_diag # sum of dp up, left, current and subtract the overlap

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(dp(dp_table, x1,y1,x2,y2))