# 576. Problem Review

## 576. Out of Boundary Paths

### Problem Definition

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo `10^9 + 7`.

### Approach
- This is DP.
- We could create a m x n grid and fill the array with the count of max possible paths at that point, updating the counter every time a ball goes out of bounds within the set amount of moves.

### Solution

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def dp(i, j, moves):
            if moves < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if memo[i][j][moves] is not None:
                return memo[i][j][moves]
            ans = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ans = (ans + dp(i + dx, j + dy, moves - 1)) % MOD
            memo[i][j][moves] = ans
            return ans

        return dp(startRow, startColumn, maxMove)


print(Solution().findPaths(2, 2, 2, 0, 0))

