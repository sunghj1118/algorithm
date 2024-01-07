# 446. Problem Review

## 446. Arithmetic Slices II - Subsequence

### Problem Definition
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

### Approach
- Since this has subsequences, it will probably be DP. 

### Solution
- If length of initial list is smaller than 3, return 0.
- Initialize array of defaultdict for i in range(len(values))
- Initialize int "total subsequences"
- Iterate over all pairs for i in range(n)
    - Iterate over all pairs for j in range(i). (all values before i)
    - Calculate difference D between i and j.
    - Add the count of arith subseq ending at j with diff D.
    - Add these subseq's to the subseq's ending at i with diff D.
    - Add to total count but only when the length > 2.
- return total

```python
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
