# 2870. Problem Review

## 2870. Minimum Number of Operations to Make Array Empty

### Problem Definition
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

### Approach
- Save all the counts of the elements into a dictionary
- If it is divisible by 2 or 3, remove it.

### Attempt 1
488 / 747 testcases passed <br>
This attempt failed at [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12], returning 8 when the answer is 7.

The counts are as follows: 14:10, 12:9. <br>
10 is divided by 2, returning a count of 5. However, if 2 is subtracted twice becoming 6, it can be divided by 3 twice returning a count of 4 operations to become 0.


```python
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        chars = {}
        minOps = 0

        # Count the number of times each number appears
        for num in nums:
            if num not in chars:
                chars[num] = 1
            else:
                chars[num] += 1

        # Remove all numbers divisible by 2 or 3
        while chars:
            for num in list(chars):
                if chars[num] == 1:
                    return -1
                elif chars[num] % 3 == 0:
                    minOps += chars[num] / 3
                    del chars[num]
                elif chars[num] % 2 == 0:
                    minOps += chars[num] / 2
                    del chars[num]
                elif chars[num] >= 3:
                    minOps += 1
                    chars[num] -= 3
                elif chars[num] == 2:
                    minOps += 1
                    chars[num] -= 2
                else:
                    del chars[num]

        return int(minOps)


solution = Solution()
print(solution.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4, 2, 3,
      4, 2, 3, 2, 2, 3, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 3, 3, 3]))

```

### Solution
- Modified the solution from above to not divide entirely by 2, but rather keep subtracting 2 until it becomes divisible by 3 or reaches the base cases.

```python
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        chars = {}
        minOps = 0

        # Count the number of times each number appears
        for num in nums:
            if num not in chars:
                chars[num] = 1
            else:
                chars[num] += 1

        # Remove all numbers divisible by 2 or 3
        while chars:
            for num in list(chars):
                if chars[num] == 1:
                    return -1
                elif chars[num] % 3 == 0:
                    minOps += chars[num] / 3
                    del chars[num]
                elif chars[num] % 2 == 0:
                    minOps += 1
                    chars[num] -= 2
                elif chars[num] >= 3:
                    minOps += 1
                    chars[num] -= 3
                else:
                    del chars[num]

        return int(minOps)
