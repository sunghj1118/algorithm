from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]


print(Solution().rob([1, 2, 3, 1]))  # 4
