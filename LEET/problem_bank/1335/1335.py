class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        # If we have fewer jobs than days, it's impossible to schedule
        if n < d:
            return -1

        # Initialize DP table with infinities
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]

        # Base case: 0 difficulty for 0 jobs in 0 days
        dp[0][0] = 0

        # Fill the DP table
        for day in range(1, d + 1):
            for i in range(day, n + 1):
                max_diff = 0
                for j in range(i, day - 1, -1):
                    max_diff = max(max_diff, jobDifficulty[j - 1])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + max_diff)

        return dp[d][n]


# Example Usage
solution = Solution()
print(solution.minDifficulty([1, 1, 1], 3))  # Example input
