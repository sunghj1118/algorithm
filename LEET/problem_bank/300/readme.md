# 300. Problem Review

## 300. Longest Increasing Subsequence

### Problem Definition
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18] <br>
Output: 4 <br>
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

### Approach
- Apparently this is DP. How?

### Solution
- Create a list of [1] of size n+1.
- Cycle for every num in nums.
- Compare the current number with every num before it.
    - If it is larger than previous number, then replace the current number with max(current val vs prev val + 1)
- Return max value from the list once finished.

```python
def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the dp array
        dp = [1] * len(nums)

        # Fill dp array with the length of the longest subsequence at each position
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The length of the longest increasing subsequence is the maximum in dp
        return max(dp)
