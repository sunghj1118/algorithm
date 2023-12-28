class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        def encode_length(count):
            if count == 0:
                return 0
            elif count == 1:
                return 1
            elif count < 10:
                return 2
            elif count < 100:
                return 3
            else:
                return 4

        for i in range(1, n + 1):
            for j in range(k + 1):
                # Delete the current character
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                # Keep the current character
                count, deletions = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        count += 1
                    else:
                        deletions += 1
                        if deletions > j:
                            break
                    dp[i][j] = min(dp[i][j], dp[l - 1]
                                   [j - deletions] + encode_length(count))

        return dp[n][k]


# Example usage
sol = Solution()
print(sol.getLengthOfOptimalCompression("bababbaba", 1))  # Expected output: 7
