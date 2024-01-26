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
