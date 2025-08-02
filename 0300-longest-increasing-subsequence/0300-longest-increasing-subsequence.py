class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the dp array
        dp = [1] * len(nums)

        # Fill dp array with the length of the longest subsequence at each position
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        # The length of the longest increasing subsequence is the maximum in dp
        return max(dp)