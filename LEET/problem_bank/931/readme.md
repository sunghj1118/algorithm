# 931. Problem Review

## 931. Minimum Falling Path Sum

### Problem Definition
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

### Approach
- This is dp.
- We need to find the smallest value possible at each point and add it to the matrix.

### Solution
- Add smallest possible value from prev row to the current space value.
- Fill out matrix with the smallest possible values as such.
- Return min value from last row.

```python
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + \
                        min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + \
                        min(dp[i - 1][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = matrix[i][j] + \
                        min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])

        return min(dp[-1])
