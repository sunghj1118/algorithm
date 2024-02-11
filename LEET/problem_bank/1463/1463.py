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
                                cherries = cherryCount(r, c1) if c1 == c2 else cherryCount(
                                    r, c1) + cherryCount(r, c2)
                                maxCherries = max(
                                    maxCherries, dp[r+1][nextC1][nextC2] + cherries)
                    dp[r][c1][c2] = maxCherries

        # The answer is the maximum number of cherries collected starting from the top row
        return dp[0][0][cols-1]
