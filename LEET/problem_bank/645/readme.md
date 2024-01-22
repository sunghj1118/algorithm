# 645. Problem Review

## 645. Set Mismatch

### Problem Definition
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

### Approach
- Make a Counter.
- Make a for loop rising from 1 to len(n)+1.
- If the value i is not in Counter, then it is the skipped value.
- Else, if the count of value i is 2, it is duplicate.

### Solution

```python
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)
        dup = -1
        missing = -1

        for i in range(1, len(nums)+1):
            if i not in dict:
                missing = i
            elif dict[i] == 2:
                dup = i

        return [dup, missing]
