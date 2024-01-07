from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Length of nums
        n = len(nums)
        if n < 3:
            return 0

        # Initialize dp array
        dp = [defaultdict(int) for _ in range(n)]
        total = 0

        # Iterate over all pairs
        for i in range(n):
            # Iterate over all pairs before i
            for j in range(i):
                # Get the difference
                diff = nums[i] - nums[j]
                # Get the count of the subsequences ending at j with difference diff
                count = dp[j][diff]
                # Add these to subsequences ending at i with difference diff
                dp[i][diff] += count + 1
                # Add to total count, only if length of subsequence is greater than 2
                total += count
        return total


# Test the function with an example
solution = Solution()
test_case = [2, 4, 6, 8, 10]
print(solution.numberOfArithmeticSlices(test_case))
