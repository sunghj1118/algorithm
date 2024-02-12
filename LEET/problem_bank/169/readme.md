# 169. Problem Review

## 169. Majority Element

### Problem Definition

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### Approach
- 

### Solution


```python
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        majority = 0
        for value in dictionary:
            if dictionary[value] > (len(nums) / 2):
                majority = value

        return majority
```