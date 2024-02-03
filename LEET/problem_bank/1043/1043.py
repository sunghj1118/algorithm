from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Get the length of the array
        n = len(arr)

        # Initialize the dp array
        dp = [0] * (n + 1)

        # Iterate over the array
        for i in range(n):
            # Initialize the max value of the current partition
            cur_max = 0

            # Iterate over all possible sizes of the last subarray
            for j in range(1, min(k, i+1) + 1):
                # Update the max value
                cur_max = max(cur_max, arr[i-j+1])

                # Update dp[i] with the max sum we can get by choosing this size for the last subarray
                dp[i] = max(dp[i], (dp[i-j] if i >= j else 0) + cur_max * j)

        # Return the max sum we can get by partitioning the whole array
        return dp[n-1]


print(Solution().maxSumAfterPartitioning(
    [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))  # 84
