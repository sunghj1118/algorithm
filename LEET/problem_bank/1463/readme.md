# 1463. Problem Review

## 1463. Cherry Pickup II

### Problem Definition
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

### Approach
- DP.

### Solution
In this code, we iterate over all possible positions of the two people and update dp[x1][y1][x2] accordingly. If the two people are at the same position, we only add the cherries at that position once; otherwise, we add the cherries at both positions. Finally, we return the maximum number of cherries the two people can pick up, or 0 if it's not possible to pick up any cherries.

```python
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

        # Function to get the cherry count safely
        def cherryCount(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return grid[r][c]
            return 0

        # Initialize the dp for the bottom row
        for c1 in range(cols):
            for c2 in range(cols):
                if c1 == c2:
                    dp[rows-1][c1][c2] = grid[rows-1][c1]
                else:
                    dp[rows-1][c1][c2] = grid[rows-1][c1] + grid[rows-1][c2]

        # Fill the dp table from bottom to top
        for r in range(rows-2, -1, -1):
            for c1 in range(cols):
                for c2 in range(cols):
                    maxCherries = 0
                    for move1 in range(-1, 2):
                        for move2 in range(-1, 2):
                            nextC1, nextC2 = c1 + move1, c2 + move2
                            if 0 <= nextC1 < cols and 0 <= nextC2 < cols:
                                cherries = cherryCount(r, c1) if c1 == c2 else cherryCount(r, c1) + cherryCount(r, c2)
                                maxCherries = max(maxCherries, dp[r+1][nextC1][nextC2] + cherries)
                    dp[r][c1][c2] = maxCherries

        # The answer is the maximum number of cherries collected starting from the top row
        return dp[0][0][cols-1]


```