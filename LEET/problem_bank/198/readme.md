# 198. Problem Review

## 198. House Robber

### Problem Definition
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Approach
- This is dp.
- How do we find the largest value possible at each step?
- Create an array of length len(List) of [0].
- dp[0] = List[0]
- Compare the List[0] and List[1] and make dp[1] the larger of the two.
- Compare the previous dp[-1] value (max possible val up to that point) with the sum of current val and the max possible two steps before. List[curr] + dp[i-2].
- Return List[-1]

### Solution

```python
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
        
